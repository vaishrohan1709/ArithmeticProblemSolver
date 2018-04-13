import config
from stanfordcorenlp import StanfordCoreNLP


#  Create a file config.py and and set path = to path to stanford-corenlp-full-2018-02-27
nlp = StanfordCoreNLP(config.path)
print(nlp.ner("Matt is a doctor"))
nlp.close()

