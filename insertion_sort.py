def insertion_sort(array):
    i = 0
    while i < len(array):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            item = array[j]
            array[j] = array[j - 1]
            array[j - 1] = item
            j -= 1
        i += 1
    return array


given_array = [7, 3, 1, 5, 4, 6, 2]
print(insertion_sort(given_array))
