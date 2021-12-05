def combine_dicts(dict1, dict2):
    """
    Combines two dictionaries into a single dictionary.
    """
    for k, v in dict2.items():
        if k in dict2:
            dict1[k] = dict1.get(k, 0) + dict2[k]

    return dict1


if __name__ == "__main__":
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    print(combine_dicts(d1, d2))