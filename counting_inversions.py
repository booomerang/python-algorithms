from math import floor


def count_inversions(arr, left, right):
    if len(arr) == 1:
        return arr

    mid = floor((left + right) / 2)

    left_half_arr = count_inversions(arr[:mid + 1], left, mid)  # split left half
    right_half_arr = count_inversions(arr[mid + 1:], left, mid)  # split right half
    return merge_arrays(left_half_arr, right_half_arr)


def merge_arrays(left_arr, right_arr):
    global inversions_number
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
            inversions_number += left_len - i
    return res_arr


# given_array = [6, 5, 3, 1, 8, 7, 2, 4]
given_array = [1, 3, 5, 6, 2, 4, 7, 8]
# given_array = [1,3,6,7,2,4,5,8]
# given_array = [8, 4, 2, 1]
# given_array = [4,8,1,2]
# given_array = [4,8,12,1,2,3]
inversions_number = 0
sorted_array = count_inversions(given_array, 0, len(given_array) - 1)
print(inversions_number)


# Python3 program to count inversions in an array
# This code is contributed by Smitha Dinesh Semwal
# Taken from https://www.geeksforgeeks.org/counting-inversions/

def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count


# Driver Code
n = len(given_array)
print("Number of inversions are", getInvCount(given_array, n))
