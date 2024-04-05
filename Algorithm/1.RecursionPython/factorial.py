def factorial(n):
    # Base condition
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive call
        return n * factorial(n-1)
    
# Test the function
result = factorial(5)
print(f"The factorial of 5 is: {result}")