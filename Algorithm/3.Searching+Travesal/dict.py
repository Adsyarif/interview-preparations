# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Using dict() constructor
another_dict = dict(name="Alice", age=25, city="London")

# Accessing values
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30

# Adding/modifying items
my_dict["email"] = "john@example.com"
my_dict["age"] = 31  # Modifying existing value

# Removing items
my_dict.pop("city")
del my_dict["age"]

# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

# Example methods
keys = my_dict.keys()
values = my_dict.values()
my_dict.update(another_dict)
my_dict.clear()
