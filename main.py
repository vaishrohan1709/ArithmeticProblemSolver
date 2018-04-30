import parser
import analyzer


# Step 1: Read questions from file
def main():
    # Load questions from file
    with open('data/q1.txt', 'r') as fi:
        questions = fi.readlines()

        word_problem = parser.parse(questions[12])
        print(word_problem)
        entities = analyzer.extract(word_problem)
        for entity in entities:
            print(entity.name, entity.owner, entity.value, entity.verb)


if __name__ == '__main__':
    main()
