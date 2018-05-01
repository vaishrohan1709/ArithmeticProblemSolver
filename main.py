import parser
import analyzer

schema = {"put": "CHANGE_OUT", "plant": "CHANGE_OUT", "place": "CHANGE_OUT", "distribute": "CHANGE_OUT",
          "transfer": "REDUCTION", "sell": "CHANGE_OUT", "give": "CHANGE_OUT", "add": "CHANGE_OUT",
          "more than": "COMPARE_PLUS", "get": "CHANGE_IN", "carry": "INCREASE", "buy": "CHANGE_IN",
          "take": "CHANGE_IN", "cut": "CHANGE_IN", "pick": "CHANGE_IN", "borrow": "CHANGE_IN",
          "decrease": "REDUCTION", "leave": "REDUCTION", "spill": "REDUCTION", "lose": "REDUCTION",
          "use": "REDUCTION", "spend": "REDUCTION", "saw": "REDUCTION", "eat": "REDUCTION",
          "break": "REDUCTION", "more": "INCREASE", "build": "CHANGE_OUT", "taller": "INCREASE",
          "load": "CHANGE_OUT", "increase": "INCREASE", "immigrate": "INCREASE", "find": "INCREASE"}


# Step 1: Read questions from file
def main():
    # Load questions from file
    with open('data/q1.txt', 'r') as fi:
        questions = fi.readlines()
        # Step 2: Simplify the question by resolving conjunctions
        word_problem = parser.parse(questions[13])
        print(word_problem)
        # Step 3 : Extract entities from the question
        entities = analyzer.extract(word_problem)
        # Step 4: categorize questions based on verb and schema
        for entity in entities:
            pass
            print(entity.owner, entity.name, entity.value, entity.verb)


if __name__ == '__main__':
    main()
