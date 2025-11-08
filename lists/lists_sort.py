numbers1 = [1, 2, 3, 4, 5, 6]

# sort the list in ascending order
numbers1.sort()
print(f'sorted list in ascending order: {numbers1}')

# sort the list in descending order
numbers1.sort(reverse = True)
print(f'sorted list in descending order: {numbers1}')

# sort a list of strings by their length
strings_list = ['apple', 'banana', 'kiwi', 'cherry', 'blueberry', 'fig']
strings_list.sort(key = len)
print(f'sorted strings list by length: {strings_list}')

# sort a list of lists by their length
list_of_lists2 = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
list_of_lists2.sort(key = len)
print(f'sorted list of lists by length: {list_of_lists2}')

# sort a list of lists by the second element of each sublist
list_of_lists3 = [[1, 3], [4, 1], [2, 2], [5, 0]]
list_of_lists3.sort(key = lambda x: x[1])
print(f'sorted list of lists by second element: {list_of_lists3}')

names1 = ['Charlie', 'Alice', 'Eve', 'Bob']
print(f'names: {names1}')

# sorted built-in function to sort and return a new list - sorted ascending order
sorted_names1 = sorted(names1)
print(f'sorted names list by first element: {sorted_names1}')

# sorted built-in function to sort and return a new list - sorted descending order
# can use the reverse built-in function as well to reverse the list after sorting. see lists_reverse.py
sorted_names2 = sorted(names1, reverse = True)
print(f'sorted names list by first element descending: {sorted_names2}')

# sorted built-in function to sort by length
sorted_names3 = sorted(names1, key = len)
print(f'sorted names list by element len: {sorted_names3}')

# sort a list of names by the second element of each name
names2 = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown']
print(f'names: {names2}')
sorted_names4 = sorted(names2, key = lambda name: name.split(' ')[1])
print(f'sorted names list by second element: {sorted_names4}')
