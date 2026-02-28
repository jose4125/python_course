import copy

numbers1 = [1, 2, 3, 4, 5, 6]

# copy the list - shallow copy (is not a deep copy) is not the same reference
copied_list = numbers1.copy()
print(f'copied list: {copied_list}')
print (f'are both lists the same object? {numbers1 is copied_list}')
print (f'are both lists equal? {numbers1 == copied_list}')

# copy the list using list function  - shallow copy (is not a deep copy) is not the same reference
copied_list2 = list(numbers1)
print(f'copied list using list function: {copied_list2}')
print (f'are both lists the same object? {numbers1 is copied_list2}')
print (f'are both lists equal? {numbers1 == copied_list2}')

# copy the list using slicing - shallow copy (is not a deep copy) is not the same reference
copied_list3 = numbers1[:] # slicing to copy the entire list
print(f'copied list using slicing: {copied_list3}')
print (f'are both lists the same object? {numbers1 is copied_list3}')
print (f'are both lists equal? {numbers1 == copied_list3}')

# deep copy using copy module
list_c = [[1, 2, 3], [4, 5, 6]]
list_d = copy.deepcopy(list_c)

list_c.append([7, 8, 9])
print('are both lists the same object?', list_c is list_d)
print('are both lists equal?', list_c == list_d)
print(f'list_c: {list_c}')
print(f'list_d: {list_d}')

list_c[0][1] = 'A'
print(f'list_c: {list_c}')
print(f'list_d: {list_d}')

