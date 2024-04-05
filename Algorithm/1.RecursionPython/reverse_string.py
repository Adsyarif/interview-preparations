def reverse_string(s):
    # Base case: if the string is empty or has only one character, return it
    if len(s) <= 1:
        return s
    # Recursive case: return the last character concatenated with the reversed substring
    else:
        return s[-1] + reverse_string(s[:-1])

# Example usage:
string = "Hello, world!"
print("Original string:", string)
print("Reversed string:", reverse_string(string))
