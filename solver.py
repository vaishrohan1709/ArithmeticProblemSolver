from analyzer import Entity
from stanfordcorenlp import StanfordCoreNLP
import config

list_positive = ["more","most","greater", "greatest" , "tall" , "taller" , "tallest"]
list_negative = ["less","lesser","least" , "short" , "shorter" , "shortest"]
list_sum = ["total", "together", "all", "overall" ]

def solve(word_problem,entities):
    answer_list=''
    question_owner = ''
    last_sentence = word_problem.split(" . ")[-1]
    answer_list += " Answer : "
    nlp = StanfordCoreNLP(config.path, memory='8g')
    dependencies = nlp.dependency_parse(last_sentence)
    flag = 0

    for word in last_sentence.split(" "):
        owner = ''
        if word in list_positive:
            flag = 1
            max = -100000
            for entity in entities:
                if entity.value > max:
                    max = entity.value
                    owner = entity.owner
            answer_list += owner
            break

        elif word in list_negative:
            flag = 1
            min = 100000
            for entity in entities:
                if entity.value < min:
                    min = entity.value
                    owner = entity.owner
            answer_list += owner
            break

        elif word in list_sum:
            flag = 1
            sum = 0
            for entity in entities:
                sum += entity.value
            answer_list += str(sum)
            break

    if flag ==1 :
        nlp.close()
        return answer_list

    elif flag == 0:
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

    return answer_list