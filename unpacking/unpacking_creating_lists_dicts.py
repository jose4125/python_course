list1 = [1, 2, 3]
list2 = [4, 5, 6]

# create a new list by unpacking existing lists
combined_list = [*list1, *list2]
print(f'Combined list using unpacking: {combined_list}')


# Merge dictionaris
dict1 = {'nombre': 'John', 'last_name': 'Doe', 'age': 33, 'hobby': 'futbol'}
dict2 = {'nombre': 'Jane', 'last_name': 'Doe', 'age': 30}

merge_dict = {**dict1, **dict2}
print(f'Combined dict using unpacking: {merge_dict}')

# concat dictionaries
dict4 = {'a': 1, 'b': 2, 'c': 3}
dict5 = {'d': 4, 'e': 5, 'f': 6}
combined_dict = {**dict4, **dict5}
print(f'Combined dict using unpacking: {combined_dict}')

# Convert a string to a list
list2 = [*'hello world!']
print(f'list2: {list2}')