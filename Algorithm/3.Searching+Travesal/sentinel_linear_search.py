def sentinel_linear_search(arr, target):
    n = len(arr)
    
    # Setting the last element of the array as the sentinel
    last_element = arr[n - 1]
    arr[n - 1] = target
    
    i = 0
    while arr[i] != target: 
        i += 1
    
    # Restoring the original last element
    arr[n - 1] = last_element
    
    if i < n - 1 or arr[n - 1] == target:
        return i
    else:
        return -1

# Example usage:
my_list = [4, 2, 1, 9, 5]
target_value = 7
result = sentinel_linear_search(my_list, target_value)
if result != -1:
    print(f"Target value {target_value} found at index {result}")
else:
    print(f"Target value {target_value} not found")


