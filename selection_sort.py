def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest_element_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_element_index]:
                smallest_element_index = j

        first_element_in_unsorted_part = arr[i]
        arr[i] = arr[smallest_element_index]
        arr[smallest_element_index] = first_element_in_unsorted_part
    return arr


given_array = [6, 5, 3, 1, 8, 7, 2, 4]
# given_array = [8, 1, 2, 3, 4, 5, 6, 7]
# given_array = [1, 2, 3, 4, 5, 6, 7, 8]
print(selection_sort(given_array))
