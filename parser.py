import config
from stanfordcorenlp import StanfordCoreNLP
import nltk
import json


def parse(question):
    # Resolve Conjunctions as noted in Sundaram, Khemani (2015)
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # Split question into constituent sentences
    sentences = tokenizer.tokenize(question)
    print(sentences)
    return_sentence = ''
    for sentence in sentences:
        conj = ' '
        # Switch on specific conjunctions from dataset
        if 'if' in sentence.split():
            conj = 'if'
        elif 'and' in sentence.split():
            conj = 'and'
        elif 'but' in sentence.split():
            conj = 'but'
        elif 'then' in sentence.split():
            conj = 'then'

        if conj != ' ':
            # Perform splits left and right of the conjunction
            left_segment = sentence.split(conj)[0]
            right_segment = sentence.split(conj)[1]

            # Create a file config.py and and set path = to path to stanford-corenlp-full-2018-02-27
            nlp = StanfordCoreNLP(config.path, memory='8g')

            # Tokenize each segment
            left_segment_tokens = nlp.word_tokenize(left_segment)
            right_segment_tokens = nlp.word_tokenize(right_segment)

            if not isVerb(left_segment, nlp):
                return_sentence = return_sentence + sentence + ' '
                continue

            # TODO: get verb phrase, is prep
            nlp.close()
        else:
            return_sentence = return_sentence + sentence + ' '
    return return_sentence


def isVerb(segment, nlp):
    """
    :param segment: sentence segment to check for verbs
    :param nlp: stanfordcorenlp engine
    :return: truth value of verb presence in phrase
    """
    index = 1
    for word in segment.split():
        tag = nlp.pos_tag(word)[0][1]

        if tag.find('VB') != -1 and segment.index(word) != 0:
            if not str(segment[segment.index(word) - 1]).find('TO') != 1 and index < len(segment):
                if not isVerb(segment[index:len(segment) - 1], nlp):
                    return True
        if tag.find('VB') and segment.index(word) == 0:
            if len(segment) > 1 and index < len(segment) and not isVerb(segment[index:len(segment) - 1], nlp):
                return True
            if len(segment) == 1:
                return True
        index += 1
    return False








