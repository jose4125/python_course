list1 = ['juan', 'pedro', 'maria', 'luisa', 'carmen']
list2 = 'jose ana julian sofia laura'.split()

# concat lists using Unpacking lists
combined_list = [*list1, *list2]
print(f'Combined list using unpacking: {combined_list}')

# concat lists
print(f'list1 + list2: {list1 + list2}')

# extend list1 with list2. Extend does not return a new list, it modifies the original list1
list1.extend(list2)
print(f'list1 after extend: {list1}')

