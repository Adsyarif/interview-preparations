def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_data = arr[i]
        j = i - 1
        while j >= 0 and current_data < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_data

# Example usage:
my_list = [64, 34, 25, 12]
insertion_sort(my_list)
print("Sorted array:", my_list)