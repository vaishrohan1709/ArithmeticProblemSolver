import config
from stanfordcorenlp import StanfordCoreNLP
import json


def parse(question):
    # Resolve Conjunctions as noted in Sundaram, Khemani (2015)
    conj = ' '
    question = str(question).replace(', but', '.')
    # Switch on specific conjunctions from dataset
    if 'if' in question:
        conj = 'if'
    elif 'and' in question:
        conj = 'and'
    elif 'but' in question:
        conj = 'but'
    elif 'then' in question:
        conj = 'then'

    # Perform splits left and right of the conjunction
    left_segment = question.split(conj)[0]
    right_segment = question.split(conj)[1]

    # Create a file config.py and and set path = to path to stanford-corenlp-full-2018-02-27
    nlp = StanfordCoreNLP(config.path, memory='8g')

    # Tokenize each segment
    left_segment_tokens = nlp.word_tokenize(left_segment)
    right_segment_tokens = nlp.word_tokenize(right_segment)
    #print isVerb(left_segment_tokens, nlp)
    print(isVerb("I am running", nlp))


def isVerb(segment, nlp):
    """
    :param segment: sentence segment to check for verbs
    :param nlp: stanfordcorenlp engine
    :return: truth value of verb presence in phrase
    """
    index = 1
    for word in segment.split():
        if str(nlp.pos_tag(word)[0][1]).find('VB') != -1 and segment.index(word) != 0:
            if not str(segment[segment.index(word) - 1]).find('TO') != 1 and index < len(segment):
                if not isVerb(segment[index:len(segment) - 1], nlp):
                    return True
        if str(nlp.pos_tag(word)[0][1]).find('VB') and segment.index(word) == 0:
            if len(segment) > 1 and index< len(segment) and not isVerb(segment[index:len(segment) - 1], nlp):
                return True
            if len(segment) == 1:
                return True
        index += 1
    return False






