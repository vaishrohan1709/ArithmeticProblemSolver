from stanfordcorenlp import StanfordCoreNLP
import config
from operator import itemgetter

nlp = StanfordCoreNLP(config.path)
'''
sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
print 'Tokenize:', nlp.word_tokenize(sentence)
print 'Part of Speech:', nlp.pos_tag(sentence)
# print 'Named Entities:', nlp.ner(sentence)
print 'Constituency Parsing:', nlp.parse(sentence)
'''
print 'Dependency Parsing:', nlp.dependency_parse("Sam gave harry some money")

nlp.close()

'''
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
                    verb = stem.encode('ascii', 'ignore')


            if dependency[0].encode('ascii', 'ignore') == 'nsubj' or dependency[0].encode('ascii', 'ignore') == 'iobj':
                if nlp.pos_tag(sentence.split()[int(dependency[2] - 1)])[0][1].find("PRP") == -1:
                    nouns.append(sentence.split()[int(dependency[2] - 1)])
                    
            # get quantities
            elif nlp.pos_tag(sentence.split()[int(dependency[2] - 1)])[0][1].find("CD") != -1:
                quantities.append(float(sentence.split()[int(dependency[2] - 1)]))
            # get objects
            # TODO: GENERALIZE ASSUMPTION ON NUMBER OF ITEMS IN QUESTION TO MORE THAN 1
            elif dependency[0].encode('ascii', 'ignore') == 'dobj':
                if nlp.pos_tag(sentence.split()[int(dependency[2] - 1)])[0][1].find("NN") != -1 or \
                        nlp.pos_tag(sentence.split()[int(dependency[2] - 1)])[0][1].find("NNS") != -1:
                    # Added stemmed versions of objects for now
                    tag = nlp.pos_tag(sentence.split()[int(dependency[2] - 1)])[0][1].encode('ascii', 'ignore')
                    if tag.startswith('V') or tag.startswith('N') or tag.startswith('R') or \
                            tag.startswith('A') or tag.startswith('S'):
                        stem = WordNetLemmatizer().lemmatize(sentence.split()[int(dependency[2] - 1)],
                                                             pos=tag[0].lower())
                    else:
                        stem = WordNetLemmatizer().lemmatize(sentence.split()[int(dependency[2] - 1)])
                    objects.append(stem.encode('ascii', 'ignore'))

    # Create entities for each subject
    for i, noun in enumerate(nouns):
        entity = Entity(noun, verb)
        try:
            entity.set_value(quantities[i])
        except IndexError:
            entity.set_value(0)
        try:
            entity.set_name(objects[i])
        except IndexError:
            # In the case of an empty object after conjunction
            entity.set_name(objects[0])
        entities.append(entity)

    nlp.close()
    return entities
'''