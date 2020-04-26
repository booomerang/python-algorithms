array_from_file = []
f = open('_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt', 'r')

for line in f:
    array_from_file.append(int(line[:-1]))

f.close()


def count_inversions(arr, left, right):
    if len(arr) == 1:
        return arr

    mid = (left + right) // 2

    left_half_arr = count_inversions(arr[:mid + 1], left, mid)  # split left half
    right_half_arr = count_inversions(arr[mid + 1:], left, len(arr[mid + 1:]) - 1)  # split right half
    return merge_arrays(left_half_arr, right_half_arr)


def merge_arrays(left_arr, right_arr):
    global inversions_number  # bad practice, I know that :)
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
        elif left_arr[i] <= right_arr[j]:
            res_arr.append(left_arr[i])
            i += 1
        else:
            res_arr.append(right_arr[j])
            j += 1
            inversions_number += left_len - i
    return res_arr


inversions_number = 0
sorted_array = count_inversions(array_from_file, 0, len(array_from_file) - 1)
print('My number of inversions are: ' + str(inversions_number))
