def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    my_dict = {}
    counter = 0
    counter2 = 0
    difference = len(keys) - len(values)
    if difference > 0:
        while counter2 < difference:
            values.append(None)
            counter2 += 1

    while counter < len(keys):
        my_dict[keys[counter]] = values[counter]
        counter += 1

    return my_dict
