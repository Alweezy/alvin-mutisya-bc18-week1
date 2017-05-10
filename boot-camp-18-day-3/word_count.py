def words(input_string):
    """Counts the number of words in a string and its number of occurances.
    :param input_string
    :return: my_dictionary:
    """
    dictionary = {}
    string = input_string.split()
    for word in string:
        dictionary_keys = dictionary.keys()
        if word not in dictionary_keys and word.isdigit():
            dictionary[int(word)] = 1
        elif word not in dictionary_keys:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary

# print(words("check this 123 and me"))
