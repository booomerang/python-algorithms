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


def insertion_sort_recursive(arr, index):
    if index < len(arr):
        j = index
        while j > 0 and arr[j] < arr[j - 1]:
            item = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = item
            j -= 1
        index += 1
        return insertion_sort_recursive(arr, index)
    return arr


given_array = [7, 3, 1, 5, 4, 6, 2]
print(insertion_sort(given_array))
print(insertion_sort_recursive(given_array, 0))
