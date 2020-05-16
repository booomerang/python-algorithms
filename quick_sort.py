def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
    return arr


def partition(arr, low, high):
    return partition_by_last_element_as_a_pivot(arr, low, high)


# Udacity variant https://www.youtube.com/watch?v=kUon6854joIs
def partition_by_last_element_as_a_pivot(arr, low, high):
    pivot = arr[high]  # splitPoint element
    pivot_index = high
    i = low

    while i < pivot_index:
        if arr[i] > pivot:
            # pre_pivot = arr[pivot_index - 1]
            # current_element = arr[i]

            # arr[i] = pre_pivot
            # arr[pivot_index - 1] = pivot
            # arr[pivot_index] = current_element

            arr[i], arr[pivot_index - 1] = arr[pivot_index - 1], arr[i]
            arr[pivot_index], arr[pivot_index - 1] = arr[pivot_index - 1], arr[pivot_index]

            pivot_index -= 1
        else:
            i += 1

    return pivot_index


def partition_by_random_element_as_a_pivot(arr, low, high):
    return 0


given_array = [6, 5, 3, 1, 8, 7, 2, 4]
# given_array = [8, 1, 2, 3, 4, 5, 6, 7]
# given_array = [1, 2, 3, 4, 5, 6, 7, 8]
print(quick_sort(given_array, 0, len(given_array) - 1))
