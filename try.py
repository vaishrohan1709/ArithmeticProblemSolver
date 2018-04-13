import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = '/Users/vaishrohan/Downloads/stanford-parser-full-2018-02-27/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/Users/vaishrohan/Downloads/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models.jar'

parser = stanford.StanfordParser(model_path="/Users/vaishrohan/Downloads/stanford-parser-full-2018-02-27/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your Empire State?"))
print sentences

for line in sentences:
	for sentence in line:
		print sentence


from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('/Users/vaishrohan/Downloads/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz') 
print (st.tag('Rami Eid is studying at Stony Brook University in NY'.split()))
print 'hey'
