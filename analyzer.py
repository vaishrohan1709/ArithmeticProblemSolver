from nltk.stem.wordnet import WordNetLemmatizer
from stanfordcorenlp import StanfordCoreNLP
import config


def extract(word_problem):
    linguistic_info = []
    word_problem = word_problem.split(' . ')
    # Create a file config.py and and set path = to path to stanford-corenlp-full-2018-02-27
    nlp = StanfordCoreNLP(config.path, memory='4g')
    for sentence in word_problem:
        print(sentence)
        print(nlp.dependency_parse(sentence))
         # first number represents source second number respresents destination of edge
    nlp.close()
    '''
        for word in sentence.split():
            tag = nlp.pos_tag(word)[0][1]
            print(nlp.dependency_parse(sentence))
            print(tag, word)
            
            tag = tag.encode('ascii', 'ignore')
            if tag.startswith('J') or tag.startswith('V') or tag.startswith('N') or tag.startswith('R') or\
                    tag.startswith('A') or tag.startswith('S'):
                stem = WordNetLemmatizer().lemmatize(word, pos=tag[0].lower())
            else:
                stem = WordNetLemmatizer().lemmatize(word)
            linguistic_info.append((tag, stem, word))
            
'''