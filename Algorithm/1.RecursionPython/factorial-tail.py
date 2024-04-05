def factorial_tail_recursive(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial_tail_recursive(n - 1, n * accumulator)

def factorial_non_tail_recursive(n):
    if n == 0:
        return 1
    else:
        result = n * factorial_non_tail_recursive(n - 1)
        return result
    
print(factorial_non_tail_recursive(4))
print(factorial_tail_recursive(4))