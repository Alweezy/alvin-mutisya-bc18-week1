class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b

        """poulate the list b with valid content with it's length determined
        by a.
        """
        for number in range(self.a):
            list.append(self, self.b)
            self.b += b

        self.length = self.a

    def search(self, value):
        """ Get the index of the item with an expected number of loops in\
        array
        :params value:
        :return: a dictionary containing {count: value, index: value}:
        """
        item_in_list = False
        upper_limit = (self.length - 1)
        lower_limit = 0
        count = 0
        try:
            index = self.index(value)
            item_in_list = True
        except ValueError:
            index = -1
            item_in_list
        while lower_limit <= upper_limit and value != self[upper_limit] and item_in_list:
            middle_item = (lower_limit + upper_limit) // 2
            middle_value = self[middle_item]
            if value > middle_value:
                lower_limit = middle_item + 1
                count += 1
            elif value < middle_value:
                upper_limit = middle_item - 1
                count += 1
            else:
                count += 1
                break
        return {'count': count, 'index': index}
