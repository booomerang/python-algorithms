def bubble_sort(arr):
    remaining_length = len(arr)
    swap_counter = 1
    while swap_counter > 0 and remaining_length > 0:
        swap_counter = 0
        for i in range(remaining_length - 1):
            if arr[i] > arr[i + 1]:
                current_item = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = current_item
                swap_counter += 1
        remaining_length -= 1
    return arr


given_array = [7, 8, 1, 5, 2, 3, 4, 6]
# given_array = [8, 1, 2, 3, 4, 5, 6, 7]
# given_array = [1, 2, 3, 4, 5, 6, 7, 8]
print(bubble_sort(given_array))
