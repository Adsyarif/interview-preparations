def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Estimate the position of target using interpolation formula
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
result = interpolation_search(my_list, target_value)
if result != -1:
    print(f"Target value {target_value} found at index {result}")
else:
    print(f"Target value {target_value} not found")
