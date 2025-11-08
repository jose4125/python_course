list1 = [1,2,3]
list2 = ['a', 'b', 'c', 'd']
tuple1 = 321, 322,323,324,325
set1 = {6,4,0,9,8,15,10}

merged_zip1 = zip(list1, list2, tuple1, set1)
print(f'Merged zip1: {merged_zip1}')
merged_list1 = list(merged_zip1)
print(f'Merged list1: {merged_list1}')

tuple2 = (1,2,3)
merged_zip2 = zip(list2, tuple2)
print(f'Merged zip2: {merged_zip2}')
merged_tuple1 = tuple(merged_zip2)
print(f'Merged list2: {merged_tuple1}')

# iterate
for number, letter, num_id, random_num in zip(list1, list2, tuple1, set1):
    print(f'number: {number}')
    print(f'letter: {letter}')
    print(f'id: {num_id}')
    print(f'random_num: {random_num}')

# unzip - unpacking
list3 = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*list3)
print(f'numbers: {numbers}, letters: {letters}')

list4 = [[1, 'a'], [2, 'b'], [3, 'c']]
numbers, letters = zip(*list4)
print(f'numbers: {numbers}, letters: {letters}')

list5 = ([1, 'a'], [2, 'b'], [3, 'c'])
numbers, letters = zip(*list5)
print(f'numbers: {numbers}, letters: {letters}')

# order using zip
list6 = ['c', 'd', 'a', 'e', 'b']
print(f'letters: {list6}')
num_list = [3,2,4,1,0]
print(f'numbers: {num_list}')
merged_list2 = zip(list6, num_list)
print(f'merged: {tuple(merged_list2)}')

# order by letter - first iterable
# we have to zip the list again because we print the merged_list2 in line 43. so we are not able to use it after
print(f'merged list ordered by letter {sorted(zip(list6, num_list))}')

# order by numbers - first iterable
print(f'merged list ordered by numbers {sorted(zip(num_list, list6))}')

# create a dict with zip. from 2 iterables
keys1 =  ['name', 'last_name', 'age']
values1 = ['john', 'doe', 33]

dict1 = dict(zip(keys1, values1))
print(f'dict: {dict1}')

# update an element of a dict
new_age_key = ['age']
new_age_value = [45]
dict1.update(zip(new_age_key, new_age_value))
print(f'new dict: {dict1}')

# add new dict key
hobby_key = ['hobby']
hobby_value = ['futbol']
dict1.update(zip(hobby_key, hobby_value))
print(f'dict with hobby: {dict1}')
