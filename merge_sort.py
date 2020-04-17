from math import floor


def merge_sort(arr, left, right):
    if len(arr) == 1:
        return arr

    mid = floor((left + right) / 2)

    left_half_arr = merge_sort(arr[:mid+1], left, mid)  # split left half
    right_half_arr = merge_sort(arr[mid+1:], left, mid)  # split right half
    return merge_arrays(left_half_arr, right_half_arr)


def merge_arrays(left_arr, right_arr):
    res_arr = []
    left_len = len(left_arr)
    right_len = len(right_arr)

    i = 0
    j = 0
    while len(res_arr) < (left_len + right_len):
        if j == right_len:
            res_arr.append(left_arr[i])
            i += 1
        elif i == left_len:
            res_arr.append(right_arr[j])
            j += 1
        elif left_arr[i] < right_arr[j]:
            res_arr.append(left_arr[i])
            i += 1
        else:
            res_arr.append(right_arr[j])
            j += 1
    return res_arr


given_array = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_array = merge_sort(given_array, 0, len(given_array)-1)
print(sorted_array)
