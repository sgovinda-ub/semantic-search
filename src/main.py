import sys
from loguru import logger
from flask import Flask, jsonify, Response, request
import json

#Internal modules
from filemanager import Filemanager
from transformer import Transformer
from vectordb import VectorDB
import const

logger.remove(0)
logger.add(sys.stdout, level=const.LOG_LEVEL)

filemanager = Filemanager(logger)
sentences = filemanager.process()

transformer = Transformer(logger)
embeddings = transformer.process(sentences)

vectordb = VectorDB(logger, embeddings)
vectordb.indexing()

# API handler to process queries
def querylookup():
    print(request.get_json()['query'])
    query_text = request.get_json()['query']
    query = transformer.embed([query_text])
    index_str_list = vectordb.search(query, const.TOP_K)  # search

    output = []
    for idx, i_str in enumerate(index_str_list):
        i = int(i_str)
        output.append({"Rank":idx, "output":sentences[i]})
    print(output)
    return output

def main():
    # Initialize api server
    app = Flask("SemanticSearch")
    app.add_url_rule("/query", "query", querylookup, methods=['POST'])
    app.run()

if __name__ == '__main__':
    main()
