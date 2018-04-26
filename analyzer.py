from nltk.stem.wordnet import WordNetLemmatizer
from stanfordcorenlp import StanfordCoreNLP
import config


schema = {"put": "CHANGE_OUT", "plant": "CHANGE_OUT", "place": "CHANGE_OUT", "distribute": "CHANGE_OUT",
          "transfer": "REDUCTION", "sell": "CHANGE_OUT", "give": "CHANGE_OUT", "add": "CHANGE_OUT",
          "more than": "COMPARE_PLUS", "get": "CHANGE_IN", "carry": "INCREASE", "buy": "CHANGE_IN",
          "take": "CHANGE_IN", "cut": "CHANGE_IN", "pick": "CHANGE_IN", "borrow": "CHANGE_IN",
          "decrease": "REDUCTION", "leave": "REDUCTION", "spill": "REDUCTION", "lose": "REDUCTION",
          "use": "REDUCTION", "spend": "REDUCTION", "saw": "REDUCTION", "eat": "REDUCTION",
          "break": "REDUCTION", "more": "INCREASE", "build": "CHANGE_OUT", "taller": "INCREASE",
          "load": "CHANGE_OUT", "increase": "INCREASE", "immigrate": "INCREASE", "find": "INCREASE"}


def extract(word_problem):
    linguistic_info = []
    verb = ''
    tense = ''
    keyword = ''
    word_problem = word_problem.split(' . ')
    # Create a file config.py and and set path = to path to stanford-corenlp-full-2018-02-27
    nlp = StanfordCoreNLP(config.path, memory='4g')
    for sentence in word_problem:
        for word in sentence.split():
            tag = nlp.pos_tag(word)[0][1]
            tag = tag.encode('ascii', 'ignore')
            if tag.startswith('V') or tag.startswith('N') or tag.startswith('R') or \
                    tag.startswith('A') or tag.startswith('S'):
                stem = WordNetLemmatizer().lemmatize(word, pos=tag[0].lower())
            else:
                stem = WordNetLemmatizer().lemmatize(word)
            if tag.find("VB") != -1 or tag.find("RBR") != -1 or tag.find("JJ") != -1:
                if tag.find("VB") != -1:
                    verb = stem
                if tag.find("VBD") != -1 or (tag.find("VBN") != -1 and tense == ''):
                    tense = "past"
                elif tense == '' and tag.find("VB") != -1:
                    tense = "present"
            if stem in schema:
                if not stem == "more" and stem == verb and not stem == "take":
                    keyword = stem
                elif stem == "take" and not sentence.find("to") != -1:
                    keyword = stem
                elif sentence.find("more than") != -1:
                    keyword = "more than"
                elif keyword == '' and stem == "take":
                    keyword = "more"

        # Get dependency parse for each sentence in question
        parse = nlp.dependency_parse(sentence)
        # first number represents source second number respresents destination of edge
        # TODO: sort edge list
    nlp.close()