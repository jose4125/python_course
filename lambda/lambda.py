def square(x):
    return x ** 2

print(f'square: {square(3)}')

# lambda function
square2 = lambda x: x ** 2
print(f'square2: {square2(3)}')

square3 = lambda x: square(x)
print(f'square3: {square3(3)}')