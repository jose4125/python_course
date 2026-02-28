def square(x):
    return x ** 2

print(f'square: {square(3)}')

# lambda function
square2 = lambda x: x ** 2
print(f'square2: {square2(3)}')

square3 = lambda x: square(x)
print(f'square3: {square3(3)}')

# example
print(' Search example '.center(25, '='))
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find an element with {expected}')

friends = [
    {
        'name': 'Rolf Smith',
        'age': 23
    },
    {
        'name': 'Adam Wool',
        'age': 45
    },
    {
        'name': 'Anne Pun',
        'age': 76
    }
]

findByName = lambda elem : elem['name']

print(search(friends, 'Adam Wool', findByName))