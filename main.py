import parser
import analyzer
import categorize
from stanfordcorenlp import StanfordCoreNLP
from solver import solve
import config

schema = {"serve": ""}

'''
schema = {"put": "CHANGE_OUT", "plant": "CHANGE_OUT", "place": "CHANGE_OUT", "distribute": "CHANGE_OUT",
          "transfer": "REDUCTION", "sell": "CHANGE_OUT", "give": "CHANGE_OUT", "add": "CHANGE_OUT",
          "more than": "COMPARE_PLUS", "get": "CHANGE_IN", "carry": "INCREASE", "buy": "CHANGE_IN",
          "take": "CHANGE_IN", "cut": "CHANGE_IN", "pick": "CHANGE_IN", "borrow": "CHANGE_IN",
          "decrease": "REDUCTION", "leave": "REDUCTION", "spill": "REDUCTION", "lose": "REDUCTION",
          "use": "REDUCTION", "spend": "REDUCTION", "saw": "REDUCTION", "eat": "REDUCTION",
          "break": "REDUCTION", "more": "INCREASE", "build": "CHANGE_OUT", "taller": "INCREASE",
          "load": "CHANGE_OUT", "increase": "INCREASE", "immigrate": "INCREASE", "find": "INCREASE"}
'''


# Step 1: Read questions from file
def main():
    # Load questions from file
    with open('data/q1.txt', 'r') as fi:
        questions = fi.readlines()
        # Step 2: Simplify the question by resolving conjunctions
        word_problem = parser.parse("Rohan has 4 pencils . He lost 3 of them ")
        print(word_problem)
        # Step 3 : Extract entities from the question
        owners, quantities, verbs, obj = analyzer.extract(word_problem)

        # Step 4: categorize questions based on verb and schema and perform computations
        entities = categorize.assign(owners, verbs, quantities)

        # Step 5: processing the question and answering it
        answer_list = ''
        answer_list = solve(word_problem,entities)
        print(answer_list)


if __name__ == '__main__':
    main()
