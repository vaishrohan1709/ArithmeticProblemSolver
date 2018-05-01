from analyzer import Entity


def assign(owners, verbs, quantities):
    entities = []
    names = set([item for sublist in owners for item in sublist])
    for name in names:
        entity = Entity(name)
        entities.append(entity)

    for i, verb in enumerate(verbs):
        if verb == "has":
            for owner in owners[i]:
                for entity in entities:
                    if entity.owner == owner:
                        entity.value = quantities[i]
        if verb == "gave":
            for entity in entities:
                if entity.owner == owners[i][0]:
                    entity.value -= quantities[i]
                elif entity.owner == owners[i][1]:
                    entity.value += quantities[i]

    for e in entities:
        print(e.owner, e.value)

    return entities