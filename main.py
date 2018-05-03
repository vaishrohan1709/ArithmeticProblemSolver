import parser
import analyzer
import categorize
from solver import solve

# Step 1: Read questions from file
def main():
    # Load questions from file
    with open('data/q2.txt', 'r') as fi:
        questions = fi.readlines()
        # Step 2: Simplify the question by resolving conjunctions

        word_problem = parser.parse(questions[1])
        print(word_problem)
        # Step 3 : Extract entities from the question
        owners, quantities, verbs, obj , word_problem = analyzer.extract(word_problem)
        # Step 4: categorize questions based on verb and schema and perform computations
        entities = categorize.assign(owners, verbs, quantities)

        # Step 5: processing the question and answering it
        answer_list = ''
        answer_list = solve(word_problem,entities)
        print(answer_list)


if __name__ == '__main__':
    main()
