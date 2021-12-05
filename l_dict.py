"""
Function get_list()

Takes a list of dictionaries as an argument and returns a list of all the unique dictionaries in the input list.

"""

def get_list(dictionary_list):
    unique_list = []
    for dictionary in dictionary_list:
        if dictionary not in unique_list:
            unique_list.append(dictionary)
    return unique_list


if __name__ == "__main__":
    
    dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]

    print(get_list(dict_list))

