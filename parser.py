import config
from stanfordcorenlp import StanfordCoreNLP
import nltk


def parse(question):
    # Resolve Conjunctions as noted in Sundaram, Khemani (2015)
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # Split question into constituent sentences
    sentences = tokenizer.tokenize(question)
    return_sentence = ''
    v1 = ''
    v2 = ''
    p1 = ''
    p2 = ''
    prp1 = ''
    prp2 = ''
    verb_phrase2 = ''
    verb_phrase = ''
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
            right_segment = sentence.split(conj)[1].lstrip()

            # Create a file config.py and and set path = to path to stanford-corenlp-full-2018-02-27
            nlp = StanfordCoreNLP(config.path, memory='4g')

            if is_verb(left_segment, nlp):
                verb_phrase = get_verb_phrase(left_segment, nlp).lstrip()
                v1 = verb_phrase.split(" ", 1)[0]
                #print('v1=',v1)
                p1 = left_segment[0: left_segment.index(v1)].rstrip()

                if not is_verb(right_segment, nlp):
                    v2 = v1
                    p2 = p1
                    #print('v2=', v2)

                else:
                    verb_phrase2 = get_verb_phrase(right_segment, nlp)
                    v2 = verb_phrase2.split(" ", 1)[0]
                    p2 = right_segment[0: right_segment.index(v2)].lstrip()

                if is_prep(left_segment, nlp):
                    prp1 = get_prep_phrase(left_segment, nlp).lstrip()
                if is_prep(right_segment, nlp):
                    prp2 = get_prep_phrase(right_segment, nlp)

                if p2 == '':
                    p2 = p1
                resolved_left = p1 + " " + verb_phrase
                # CHANGE MADE added v2 to if condition
                if verb_phrase2 == '':
                    resolved_right = p2.lstrip() + " " + v2 + " " + right_segment
                else:
                    resolved_right = p2.lstrip() + " " + v2 + " " + prp2

                nlp.close()
                return_sentence = return_sentence + " " + resolved_left + ". " + resolved_right


        else:
            return_sentence = return_sentence + " " + sentence

    return return_sentence


def is_verb(segment, nlp):
    """
    :param segment: sentence segment to check for verbs
    :param nlp: stanfordcorenlp engine
    :return: truth value of verb presence in phrase
    """
    for word in segment.split():
        tag = nlp.pos_tag(word)[0][1]
        if tag.find('VB') != -1:
            return True

    '''
    index = 1
    for word in segment.split():
        tag = nlp.pos_tag(word)[0][1]
        if 'VBG' in tag:
            index += 1
            continue

        if tag.find('VB') != -1 and segment.index(word) != 0:
            if str(segment[segment.index(word) - 1]).find('TO') == -1 and index < len(segment):
                if not isVerb(segment[index:len(segment) - 1], nlp):
                    return True
        if tag.find('VB') != -1 and segment.index(word) == 0:
            if len(segment) > 1 and index < len(segment) and not isVerb(segment[index:len(segment) - 1], nlp):
                return True
            if len(segment) == 1:
                return True
        index += 1
    
    return False
    '''
    return False


def get_verb_phrase(segment, nlp):
    verb_phrase = ""
    index = 0
    for word in segment.split():
        tag = nlp.pos_tag(word)[0][1]
        if index > 0:
            if tag.find('VB') != -1 or tag.find("DT") != -1 or tag.find("NN") != -1 or tag.find("IN") != 1 \
                    or tag.find("RB"):
                verb_phrase = verb_phrase + word + " "
                index += 1
        if tag.find("VB") != -1:
            verb_phrase = verb_phrase + word + " "
            index += 1
    return verb_phrase


def is_prep(segment, nlp):
    for word in segment.split():
        tag = nlp.pos_tag(word)[0][1]
        if tag.find('IN') != -1 or tag.find('TO') != -1:
            return True
    return False


def get_prep_phrase(segment, nlp):
    cross_prep = False
    cross_verb = False
    prepPhrase = ""
    for word in segment.split():
        tag = nlp.pos_tag(word)[0][1]
        if tag.find("VB") != -1:
            cross_verb = True
        if is_verb(segment, nlp) and not cross_verb:
            continue
        if not cross_prep and tag.find("IN") != -1 and not word == "by" or tag.find("TO") != -1:
            cross_prep = True
            prepPhrase = prepPhrase + word + " "
            continue
        if cross_prep and tag.find("IN") != -1  and not word == "by" or tag.find("TO") != -1:
            prepPhrase = ""
            prepPhrase = prepPhrase + word + " "
            continue
        elif cross_prep:
            prepPhrase = prepPhrase + word + " "

    prepPhrase = prepPhrase.replace(" .", ".")
    prepPhrase = prepPhrase.replace(" ,", ",")
    prepPhrase = prepPhrase.replace(" '", "'")
    return prepPhrase