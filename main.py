import parser
import analyzer


# Step 1: Read questions from file
def main():
    # Load questions from file
    with open('data/q1.txt', 'r') as fi:
        questions = fi.readlines()
        for question in questions:
            pass
            # Simplify problem
        # For quick testing of parser code
        word_problem = parser.parse(questions[12])
        extracted_info = analyzer.extract(word_problem)
        print(word_problem)


if __name__ == '__main__':
    main()
