def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    numb = 1
    numb_list = []
    while numb <= num:
        if num % numb == 0:
            numb_list.append(numb)
        numb += 1
    return numb_list
