import sys
from loguru import logger

#Internal modules
from filemanager import Filemanager
from transformer import Transformer
from vectordb import VectorDB
from rest import FlaskAppWrapper
from rest import querylookup
import const

logger.remove(0)
logger.add(sys.stdout, level=const.LOG_LEVEL)

def main():
    filemanager = Filemanager(logger)
    sentences = filemanager.process()

    transformer = Transformer(logger)
    embeddings = transformer.process(sentences)

    vectordb = VectorDB(logger, embeddings)
    vectordb.indexing()

    #app = FlaskAppWrapper("SemanticSearch")
    #app.add_endpoint('/query', 'querylookup', querylookup, methods=['GET'])
    #app.run()

    k = 4
    while True:
        query_text = input("prompt: > ")
        if query_text == 'quit':
            break
        query = transformer.embed([query_text])
        index_str_list = vectordb.search(query, k)  # search

        for i_str in index_str_list:
            i = int(i_str)
            print(sentences[i])

        input("hit any key to continue...")

if __name__ == '__main__':
    main()
