from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from stanfordcorenlp import StanfordCoreNLP
import config
from operator import itemgetter


class Entity():
    def __init__(self, owner, value=0):
        """
        :param owner: Person 1 in the question
        :param verb: Verb indicating increase / decrease
        :param value: Number of entities held
        :param name: Name of the entity
        """

        self.owner = owner
        self.value = value


def extract(word_problem):
    verb = ''
    tense = ''
    keyword = ''
    entities = []
    word_problem = word_problem.split(' . ')
    # Create a file config.py and and set path = to path to stanford-corenlp-full-2018-02-27
    nlp = StanfordCoreNLP(config.path, memory='8g')
    nouns = []
    verbs = []
    obj = ''
    stem = ''
    quantities = []
    for sentence in word_problem[:-1]:
        owners = []
        parse = nlp.parse(sentence).encode('ascii', 'ignore')
        dependencies = nlp.dependency_parse(sentence)
        # (relation, source, target)
        dependencies = sorted(dependencies, key=itemgetter(1))
        # More robust way to find the tense
        if parse.find("(VP (VBD ") != -1 or parse.find("(VP (VBN ") != -1:
            tense = "past"
        elif parse.find("(VP (VBP ") != -1 or parse.find("(VP (VBG ") != -1:
            tense = "present"
        for dependency in dependencies:
            tag = nlp.pos_tag(sentence.split()[int(dependency[2] - 1)])[0][1]
            if tag.find("CD") != -1:
                quantities.append(float(sentence.split()[int(dependency[2] - 1)]))
                word = sentence.split()[int(dependency[2])]
                tag2 = nlp.pos_tag(sentence.split()[int(dependency[2])])[0][1]
                if tag2.startswith('V') or tag2.startswith('N') or tag2.startswith('R') or \
                        tag2.startswith('A') or tag2.startswith('S'):
                    stem = WordNetLemmatizer().lemmatize(word, pos=tag2[0].lower())
                else:
                    stem = WordNetLemmatizer().lemmatize(word)
                if obj == '':
                    obj = stem.encode('ascii', 'ignore')

            if dependency[0].encode('ascii', 'ignore') == 'nsubj' or dependency[0].encode('ascii', 'ignore') == 'iobj':
                if tag.find("PRP") == -1:
                    if not sentence.split()[int(dependency[2] - 1)] in owners:
                        owners.append(sentence.split()[int(dependency[2] - 1)])

            if dependency[0].encode('ascii', 'ignore') == 'nmod':
                if tag.find("NNP") != -1:
                    if not sentence.split()[int(dependency[2] - 1)] in nouns:
                        owners.append(sentence.split()[int(dependency[2] - 1)])

            if tag.find('VB') != -1:
                verbs.append(sentence.split()[int(dependency[2] - 1)])
        nouns.append(owners)
    return nouns, quantities, verbs, obj

