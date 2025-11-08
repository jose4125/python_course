numbers1 = [1, 2, 3, 4, 5, 6]

# reverse the list
reversed_list = numbers1[::-1]
print(f'reversed list: {reversed_list}')

# reverse the list using reverse method
numbers1.reverse()
print(f'reversed list using reverse method: {numbers1}')

# reverse built-in function to return a new reversed list
# reversed() returns an iterator, so we convert it to a list or tuple
numbers2 = [1, 2, 3, 4, 5, 6]
print(f'original numbers2 list: {numbers2}')
reversed_list2 = list(reversed(numbers2))
print(f'reversed list using reverse built-in method: {reversed_list2}')

string1 = ['july', 'august', 'september', 'october']
print(f'original string1 list: {string1}')
reversed_string1 = tuple(reversed(string1))
print(f'reversed string list using reverse built-in method: {reversed_string1}')