def get_cords():
    return 5, 10, 15

# Unpacking in function calls
x, y, z = get_cords()
print(f'x: {x}, y: {y}, z: {z}')

# Unpacking omitting some values in function calls
x, *_ = get_cords()
print(f'x: {x}')

# Unpacking in function arguments
def my_function(x, y, z):
    print(f'x: {x}, y: {y}, z: {z}')

args = (21, 22, 23)
my_function(*args)

# Unpacking in function arguments with asterisk
def my_function_varargs(x, y, *args):
    print(f'x: {x}, y: {y}, args: {args}')

args_var = (24, 25, 26, 27, 28)
my_function_varargs(*args_var)

# Unpacking in function arguments with only asterisk
def my_function_args(*args):
    print(f'args: {args}')
    x, y = args
    print(f'x: {x}, y: {y}')

args_only = (29, 30)
my_function_args(*args_only)

# Unpacking in function arguments with dictionary
def my_function_kwargs(a, b, c):
    print(f'a: {a}, b: {b}, c: {c}')

kwargs = {'a': 31, 'b': 32, 'c': 33}
my_function_kwargs(**kwargs)

# Unpacking in function arguments with dictionary and asterisk
def my_function_kwargs_var(a, b, **kwargs):
    print(f'a: {a}, b: {b}, kwargs: {kwargs}')
kwargs_var = {'a': 34, 'b': 35, 'c': 36, 'd': 37}
my_function_kwargs_var(**kwargs_var)

# Unpacking in function arguments with only double asterisk
def my_function_kwargs(**kwargs):
    print(f'kwargs: {kwargs}')
    x, y = kwargs['a'], kwargs['b']
    print(f'a: {x}, b: {y}')

kwargs_only = {'a': 38, 'b': 39}
my_function_kwargs(**kwargs_only)


# Unpacking in loops
list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
for number, word in list_of_tuples:
    print(f'Number: {number}, Word: {word}')

# Unpacking with enumerate to get index
for index, (number, word) in enumerate(list_of_tuples):
    print(f'Index: {index}, Number: {number}, Word: {word}')

# Unpacking with items in dictionary
dict_items = {'a': 1, 'b': 2, 'c': 3}
for key, value in dict_items.items():
    print(f'Key: {key}, Value: {value}')
