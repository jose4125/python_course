# list comprehensions with dictionaries

squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)

# mutable types can not be used as keys
# invalid_dict = {[1, 2]: 'list as key'}  # This will raise a TypeError

# Inmutable types can be used as keys
tuple = (1, 2, 3, 4)
valid_dict = {tuple: 'tuple as key'}
print(valid_dict)

