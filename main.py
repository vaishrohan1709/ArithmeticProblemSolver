import config
from stanfordcorenlp import StanfordCoreNLP

'''
#  Create a file config.py and and set path = to path to stanford-corenlp-full-2018-02-27
nlp = StanfordCoreNLP(config.path)
print(nlp.ner("Matt is a doctor"))
nlp.close()
'''


# Step 1: extract all entities and the question entity
def main():
    # Load questions from file
    with open('data/q1.txt', 'r') as fi:
        questions = fi.readlines()
    nlp = StanfordCoreNLP(config.path,  memory='8g')
    for question in questions[0:10]:
        numbers = []
        # Parse the questions for numbers
        print(nlp.annotate(question))
    nlp.close()


if __name__ == '__main__':
    main()
