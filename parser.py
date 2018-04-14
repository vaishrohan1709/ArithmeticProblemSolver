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
    print isVerb(left_segment, nlp)


def isVerb(segment, nlp):
    """
    :param segment: sentence segment to check for verbs
    :param nlp: stanfordcorenlp engine
    :return: truth value of verb presence in phrase
    """
    # Check if the left segment contains verbs
    '''
    pos = ' '
    index = 1
    for token in tokens:
        pos = nlp.pos_tag(token)
        if 'VB' in pos and tokens.index(token) != 0:
            # Check if token before is a word level to
            tk = tokens.index(token) - 1
            if 'TO' not in nlp.word_tokenize(tk) and index < len(tokens) and not isVerb(tokens[index:len(tokens-1)], nlp):
                return True
        elif 'VB' in pos and tokens.index(token) == 0:
            if len(tokens) > 1:
                return True
            if len(tokens) > 1 and len(tokens) > index:
                if not isVerb(tokens[index:len(tokens-1)], nlp):
                    return True
    return False
    '''
    return nlp.pos_tag(segment)