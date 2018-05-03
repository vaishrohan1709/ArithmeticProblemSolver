from analyzer import Entity
from nltk.stem.wordnet import WordNetLemmatizer

#TODO "more than", multiple/divide, synonyms , some words can be both unary and binary

#schema of verbs
schema = {"grow": ["Unary","Increase"], "find": ["Unary","Increase"], "increase": ["Unary","Increase"], "more": ["Unary","Increase"], "have": ["Unary","Increase"], "pick": ["Unary","Increase"],"add": ["Unary","Increase"] ,
          "break": ["Unary","Decrease"], "eat": ["Unary","Decrease"], "spend": ["Unary", "Decrease"],"use": ["Unary","Decrease"], "lose": ["Unary","Decrease"], "spill": ["Unary","Decrease"],"leave": ["Unary","Decrease"], "decrease": ["Unary","Decrease"], "cut": ["Unary","Decrease"], "plant": ["Unary","Decrease"] , "place": ["Unary","Decrease"], "put": ["Unary", "Decrease"] ,"distribute": ["Unary","Decrease"],
          "give": ["Binary","LtoR"],  "transfer": ["Binary","LtoR"],"sell": ["Binary", "LtoR"] ,
          "get": ["Binary", "RtoL"] , "buy" : ["Binary", "RtoL"] , "take" : ["Binary", "RtoL"] , "borrow" : ["Binary", "RtoL"]}


def compute(owners, entities, quantities, index, type , operation):
    if type.find("Unary") != -1:
        if operation.find("Increase") != -1:
            for owner in owners[index]:
                for entity in entities:
                    if entity.owner == owner:
                        entity.value += quantities[index]
        elif operation.find("Decrease") != -1:
            for owner in owners[index]:
                for entity in entities:
                    if entity.owner == owner:
                        entity.value -= quantities[index]

    elif type.find("Binary") != -1:
        if operation.find("LtoR") != -1:
            for entity in entities:
                if entity.owner == owners[index][0]:
                    entity.value -= quantities[index]
                elif entity.owner == owners[index][1]:
                    entity.value += quantities[index]

        elif operation.find("RtoL") != -1:
            for entity in entities:
                if entity.owner == owners[index][0]:
                    entity.value += quantities[index]
                elif entity.owner == owners[index][1]:
                    entity.value -= quantities[index]


def assign(owners, verbs, quantities):
    entities = []
    names = set([item for sublist in owners for item in sublist])
    for name in names:
        entity = Entity(name)
        entities.append(entity)

    for i, verb in enumerate(verbs):
        verb = WordNetLemmatizer().lemmatize(verb, pos='v')
        if verb in schema:
            compute(owners , entities , quantities , i , schema[verb][0] , schema[verb][1])
        else:
            print 'Cannot compute for given verbs'



    for e in entities:
        print(e.owner, e.value)

    return entities