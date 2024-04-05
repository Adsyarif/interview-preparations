def sum_digits(n):
    # Base case: if n is a single digit, return n
    if n < 10:
        return n
    # Recursive case: sum the last digit and call sum_digits with the remaining digits
    else:
        return n % 10 + sum_digits(n // 10)

# Example usage:
num = 12345
print("Sum of digits of", num, "is:", sum_digits(num))
