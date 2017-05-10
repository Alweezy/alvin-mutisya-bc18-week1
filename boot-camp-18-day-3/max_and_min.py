def find_max_min(integers):
    """Finds maximum and minumum number and return both of them as a list,
    if all elements in list are equal, return the length of list
    :param integers:
    :return: min_and_max:
    """
    min_and_max = []
    min_number = min(integers)
    max_number = max(integers)
    if max_number == min_number:
        min_and_max.append(len(integers))
    else:
        min_and_max.append(min_number)
        min_and_max.append(max_number)
    return min_and_max

print(find_max_min([2, 3, 4, 5, 6]))
print(find_max_min([4, 4]))