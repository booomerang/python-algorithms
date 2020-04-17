from math import floor

givenList = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
targetValue = 7


def binary_search(array, element):
    l = 0
    r = len(array) - 1

    # return binary_search_recursive(array, element, l, r)
    return binary_search_iterative(array, element)


def binary_search_recursive(array, element, l, r):
    m = floor((l + r) / 2)
    if array[m] < element:
        l = m + 1
    elif array[m] > element:
        r = m - 1
    elif array[m] == element:
        return m
    else:
        return False

    return binary_search_recursive(array, element, l, r)


def binary_search_iterative(array, element):
    l = 0
    r = len(array) - 1

    while l <= r:
        m = floor((l + r) / 2)
        if array[m] < element:
            l = m + 1
        elif array[m] > element:
            r = m - 1
        else:
            return m

    return False


targetIndex = binary_search(givenList, targetValue)
print(targetIndex)
