from analyzer import Entity
from stanfordcorenlp import StanfordCoreNLP
import config

def solve(word_problem,entities):
    answer_list=''
    question_owner = ''
    last_sentence = word_problem.split(" . ")[-1]
    answer_list+=last_sentence+" : "
    nlp = StanfordCoreNLP(config.path, memory='8g')
    dependencies = nlp.dependency_parse(last_sentence)
    for dependency in dependencies:
        tag = nlp.pos_tag(last_sentence.split()[int(dependency[2] - 1)])[0][1]
        if dependency[0].encode('ascii', 'ignore') == 'nsubj' or dependency[0].encode('ascii', 'ignore') == 'iobj':
            if tag.find("PRP") == -1:
                question_owner = last_sentence.split()[int(dependency[2] - 1)]

        elif dependency[0].encode('ascii', 'ignore') == 'nmod':
            if tag.find("NNP") != -1:
                question_owner = last_sentence.split()[int(dependency[2] - 1)]

    for entity in entities:
        if entity.owner == question_owner:
            answer_list+= str(entity.value)
    nlp.close()
    return answer_list