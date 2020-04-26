def count_inversions(arr, left, right):
    inversions_number = 0

    if left == right:
        return inversions_number

    mid = (left + right) // 2

    inversions_number += count_inversions(arr, left, mid)  # split left half
    inversions_number += count_inversions(arr, mid + 1, right)  # split right half
    inversions_number += merge_arrays(arr, left, mid, right)
    return inversions_number


def merge_arrays(array, left, mid, right):
    inversions_number = 0

    i = left
    j = mid + 1
    k = left
    temp_arr = array[0:]

    while k <= right:
        if j == right + 1:
            temp_arr[k] = array[i]
            k += 1
            i += 1
        elif i == mid + 1:
            temp_arr[k] = array[j]
            k += 1
            j += 1
        elif array[i] <= array[j]:
            temp_arr[k] = array[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = array[j]
            k += 1
            j += 1
            inversions_number += (mid + 1) - i

    for tindex in range(left, right + 1):
        array[tindex] = temp_arr[tindex]

    return inversions_number


# given_array = [6, 5, 3, 1, 8, 7, 2, 4]
# given_array = [1, 3, 5, 6, 2, 4, 7, 8]
# given_array = [1,3,6,7,2,4,5,8]
# given_array = [8, 4, 2, 1, 9]
# given_array = [4,8,3,5,2]
# given_array = [4, 8, 3, 5]
# given_array = [8, 4, 2, 1]
# given_array = [4,8,12,1,2,3]
given_array = [8, 4, 2, 1, 9, 5, 3, 2]

print('Inversions number: ' + str(count_inversions(given_array, 0, len(given_array) - 1)))
