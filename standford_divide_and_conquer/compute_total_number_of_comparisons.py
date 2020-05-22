filename = '_32387ba40b36359a38625cbb397eee65_QuickSort.txt'


def prepare_array_of_items_from_file(filename):
    array_from_file = []

    f = open(filename, 'r')
    for line in f:
        array_from_file.append(int(line[:-1]))
    f.close()

    return array_from_file


def compute_number_of_comporisons_of_quick_sort(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)
        compute_number_of_comporisons_of_quick_sort(arr, l, pi - 1)
        compute_number_of_comporisons_of_quick_sort(arr, pi + 1, r)


def partition(arr, l, r):
    def is_median(a, b, c):
        if (a <= b <= c) or (a >= b >= c):
            return True
        return False

    global number_of_comparisons  # bad practice

    median_index = l
    if (r - l) > 1:
        middle_point_index = (r + l) // 2

        if is_median(arr[l], arr[middle_point_index], arr[r]):
            median_index = middle_point_index
        elif is_median(arr[l], arr[r], arr[middle_point_index]):
            median_index = r

    # arr[l], arr[r] = arr[r], arr[l]  # Right element as a pivot
    arr[l], arr[median_index] = arr[median_index], arr[l]  # median element as a pivot
    # Here we push off the most left element of an array
    pivot = arr[l]
    i = l + 1

    for j in range(l + 1, r + 1):
        # number_of_comparisons += 1
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    if l < r:
        number_of_comparisons += r - l
        arr[l], arr[i - 1] = arr[i - 1], arr[l]
    return i - 1


given_array = prepare_array_of_items_from_file(filename)

number_of_comparisons = 0
compute_number_of_comporisons_of_quick_sort(given_array, 0, len(given_array) - 1)
print(number_of_comparisons)
