numbers = [1, 2, 3, 4, 5]

# next is used to get the next element of an iterator
# next parameters are
# iterator: could be a list, tuple or set. but you have to turn it into an iterator
# default value: is an optional value. it is returned if the iterator don't have elements to iterate.
print(f'numbers: {numbers}')
iterator = iter(numbers)
print(f'iterator: {iterator}')
print(f'type: {type(iterator)}')

element1 = next(iterator)
print(f'element1: {element1}')
element2 = next(iterator)
print(f'element2: {element2}')
element3 = next(iterator)
print(f'element3: {element3}')
element4 = next(iterator)
print(f'element4: {element4}')
element5 = next(iterator)
print(f'element5: {element5}')

# return the default value as there are no more element in the list
element6 = next(iterator, None)
print(f'element5: {element6}')

# return an StopIteration error since is no default value
element7 = next(iterator)
print(f'element5: {element7}')
