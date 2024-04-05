def counting_sort(arr, exp):
    """
    Perform counting sort on the array based on the given exponent.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit at the specified exponent position
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count array to store the actual position of each digit
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array by placing elements in their sorted positions
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements from the output array back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Perform radix sort on the given array.
    """
    # Find the maximum element to determine the number of digits
    max_element = max(arr)
    exp = 1

    # Apply counting sort for each digit place, starting from the least significant digit
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage:
my_list = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(my_list)
print("Sorted array:", my_list)
