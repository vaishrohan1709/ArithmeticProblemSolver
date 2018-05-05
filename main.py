import parser
import analyzer
import categorize
from solver import solve

# Step 1: Read questions from file
def main():
    # Load questions from file
    with open('data/q2.txt', 'r') as fi:
        word_problem=''
        questions = fi.readlines()
        # Step 2: Simplify the question by resolving conjunctions
        print('List of questions:')
        for i,question in enumerate(questions):
            print 'Question:',i,' : ',question
        print '\nNote: Questions 0-16 are solvable and 17-25 are not solvable according to our implementation.'
        print 'Do you want to select a question from the list (0) or enter your own (1)? Enter 0 / 1:'
        choice = input()
        if choice == 0:
            print 'Enter the question number from the list:'
            qno = input()
            word_problem = parser.parse(questions[qno])
            print(type(questions[qno]))
        else:
            word_problem = raw_input("Enter the question: ")
            word_problem = parser.parse(word_problem)

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
