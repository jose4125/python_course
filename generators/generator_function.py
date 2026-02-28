# A generator is a special kind of function or object that produces values one at a time, on demand,
# instead of computing and storing all values at once.
# More clearly:
#   - A generator yields values one by one
#   - It remembers its state between values
#   - It is lazy: it only computes the next value when requested
#   - It is memory-efficient, especially for large or infinite sequences
import random

# counter generator
def counterMax(n):
    counter = 0
    while counter < n:
        yield counter
        counter += 1

numMax = 5
countergen = counterMax(numMax)
for x in countergen:
    print(f'generated number: {x}')


# Square generator
def gensquare(n):
    for x in range(n):
        yield x ** 2

for num in enumerate(gensquare(5)):
    print(f'square of {num[0]}: {num[1]}')


# Cubes generator
def create_cubes(n):
    for x in range(n):
        yield x ** 3

for x in create_cubes(10):
    print(x)


# generate random numbers between low and high
def rand_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)

for x in enumerate(rand_num(5, 15, 7)):
    print(f'random num {x[0]}: {x[1]}')

# generator to list
generator_to_list = list(create_cubes(5))
print(generator_to_list)



# fibonacci
# 0 = 0
# 1 = 1
# 2 = 0 + 1 = 1
# 3 = 1 + 1 = 2
# 4 = 1 + 2 = 3
# 5 = 2 + 3 = 5
# 6 = 3 + 5 = 8

def gen_fibon(n):
    a = 1
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b

num = 7

for index, x in enumerate(gen_fibon(num)):
    print(f'fibonacci de {index + 1 }, {x}')


# iterator
word = 'hello'
iter_string = iter(word)
# to access the items have to use next() method
print('first letter', next(iter_string))
print('second letter', next(iter_string))

for _ in range(len(word) - 2):
    print(next(iter_string))
