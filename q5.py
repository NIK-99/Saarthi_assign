from itertools import permutations

def main():
    # extras: hyderabad, "What is your favourite place to visit <>, <> or <>"
    entities_list = ["kolkata", "delhi", "hyderabad"]
    utterance_list = ["How far is <> from <>", "How is the weather in <> ", "What is your favourite place to visit among <>, <> or <>"]

    for utterance in utterance_list:
        # print(utterance)
        numOfBlanks = utterance.count("<>")
        tempString = utterance

        entityCombos = list(permutations(entities_list, numOfBlanks))
        # print(entityCombos)
        for combination in entityCombos:
            # print(combination)
            for entity in combination:
                # print(entity)
                tempString = tempString.replace("<>", entity, 1)

            print(tempString)
            tempString = utterance


if __name__ == '__main__':
    main()