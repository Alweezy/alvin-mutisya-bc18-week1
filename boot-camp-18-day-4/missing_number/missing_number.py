def find_missing(array_1, array_2):
    if len(array_1) is 0 and len(array_2) is 0:
        return 0
    if len(array_1) > len(array_2):
        for number in array_1:
            if number in array_2:
                continue
            else:
                return number
    else:
        for number in array_2:
            if number in array_1:
                continue
            else:
                return number
    return 0

print(find_missing([4, 66, 7], [66, 77, 7, 4]))
print(find_missing([1, 2, 3, 4], [1, 2, 3]))