import parser
import analyzer
import categorize
from stanfordcorenlp import StanfordCoreNLP
from solver import solve
import config



# Step 1: Read questions from file
def main():
    # Load questions from file
    with open('data/q1.txt', 'r') as fi:
        questions = fi.readlines()
        # Step 2: Simplify the question by resolving conjunctions

        word_problem = parser.parse("Rohan had 10 bananas . Harsha also picked up 7 from the store . Harsha ate 4 bananas . "
                                    "Janice found 7 bananas . Rohan sold 2 to Janice and 3 to Harsha . Janice bought 1 from Harsha . Harsha took 4 from Rohan . How many bananas do they have in total ?")
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
