# set is a collection of unique elements, and it is mutable
# elements in sets have to be immutable
# lists can not be an element of sets

# it returns an error -> TypeError: unhashable type: 'list'
# set1 = {[1,2], [3,4]}

set2 = {1, 'john', 10.3, True}
print(f'set2: {set2}')

# empty set
set3 = set()
print(f'set3: {set3}')
print(type(set3))

# adding elements
set3.add('jane')
print(f'set3 adding jane: {set3}')

# contain unique values
set3.add('jane')
print(f'set3 adding an existing element jane: {set3}')

# create a set from an iterable - sets don't rank in the same order
list1 = ['a', 'b', 'c', 'c']
set4 = set(list1)
print(f'set from iterable {list1}: {set4}')

# adding more elements or adding another set
set5 = {100, 200, 300, 300}
set4.update(set5)
print(f'updating set4 with another set: {set4}')

# adding more elements with an iterable
set4.update([20, 40, 60, 60, 80])
set4.update(('z', 'x', 'y', 'z'))
print(f'updating set4 with a list: {set4}')

# copy set - shallow copy (is not a deep copy) is not the same reference
set_copy = set4.copy()
print(f'copy set4: {set_copy}')
print(f'set_copy has the same reference as set4: {set_copy is set4}')
print(f'set_copy has the same content as set4: {set_copy == set4}')