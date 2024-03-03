import os
import time
import spacy
import const

class Filemanager(object):
    def __init__(self, logger):
        self.file_location = const.PATH
        self.chunk_size = const.CHUNK_SIZE
        self.logger = logger
        self.nlp_model = const.NLP_MODEL

    # Convert docs to text 
    def parse(self):
        return
    
    # Convert text files to chunks 
    def chunk(self):
        self.logger.info("Chunking sentences")
        sentences = []
        nlp = spacy.load(self.nlp_model)
        file_list = os.listdir(self.file_location)
        self.logger.info(file_list)
        start_time = time.time()
        for dirpath,_,filenames in os.walk(self.file_location):
            for file in filenames:
                filename = os.path.join(dirpath, file)
                self.logger.debug(f"\tprocessing {filename}")
                try:
                    f = open(filename)
                except FileNotFoundError:
                    self.logger.error(f"File {filename} not found! Skipping file")
                    continue
                else:
                    in_text = f.read()
                doc = nlp(in_text)
                temp_sent = list(doc.sents)
                for sentence in temp_sent:
                    sentences.append(sentence.text)
                self.logger.debug(f"done processing corpus files, time taken: {time.time() - start_time} seconds")
            
        len_sent = []
        len_above_threshold = 0
        embed_sentences = []
        for sentence in sentences:
            len_sent.append(len(sentence))
            if len(sentence) > const.CHUNK_SIZE:
                len_above_threshold += 1

        self.logger.debug(f"\tlen sentences: {len(sentences)}")
        self.logger.debug(f"\tmin len: {min(len_sent)}")
        self.logger.debug(f"\tmax len: {max(len_sent)}")
        self.logger.debug(f"\tavg len: {sum(len_sent) / len(len_sent)}")
        self.logger.debug(f"\tlen above threshold: {len_above_threshold}")
        return sentences
    
    def process(self):
        # Refer section 3.4.1 in project document
        self.parse()
        sentences = self.chunk()
        return sentences