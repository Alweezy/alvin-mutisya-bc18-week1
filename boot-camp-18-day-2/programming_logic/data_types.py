def data_type(value):
    """A function called data_type, that takes one argument,
    compares and returns results, based on the argument supplied to the function.
    """
    # check if it is a string, return the length of that string
    if isinstance(value, str):
        return len(value)
    # check there is no value, return default string
    elif value is None:
        return 'no value'
    elif isinstance(value, bool):
        return value
    # check if value is an integer, perform further evaluations
    elif isinstance(value, int):
        if value < 100:
            return 'less than 100'
        elif value is 100:
            return 'equal to 100'
        elif value > 100:
            return 'more than 100'
        else:
            return 'integer value not recognized'
    # check if value is a list, determine the size of list.
    elif isinstance(value, list):
        if len(value) >= 3:
            return value[2]
        else:
            return None
    elif type(value) in [tuple, dict, set]:
        return type(value)
    else:
        return 'sorry, input is quite invalid'