def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    list1 = list(str(num1))
    list2 = list(str(num2))
    list1.sort()
    list2.sort()
    new_set = {''.join(list1), ''.join(list2)}
    if len(new_set) == 1:
        return True
    else:
        return False
