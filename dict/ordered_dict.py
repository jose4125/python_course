from collections import OrderedDict

# Grantee the insertion order in dictionaries
ordered_dict = OrderedDict(uno=1, dos=2, tres=3)
print(ordered_dict)
ordered_dict2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ordered_dict2)

# Adding items to a dictionary
ordered_dict['cuatro'] = 4
ordered_dict2['d'] = 4
print('after adding items:')
print(ordered_dict)
print(ordered_dict2)

# Get the keys
ordered_dict_keys = ordered_dict.keys()
print(f'ordered_dict keys: {ordered_dict_keys}')
ordered_dict2_keys = ordered_dict2.keys()
print(f'ordered_dict2 keys: {ordered_dict2_keys}')

# Change values
ordered_dict['uno'] = -1
ordered_dict2['b'] = 32
print('after changing values:')
print(ordered_dict)
print(ordered_dict2)

# Remove items
ordered_dict.pop('dos')
ordered_dict2.pop('b')
print('after removing items:')
print(ordered_dict)
print(ordered_dict2)

# Adding removed items again
ordered_dict['dos'] = 2
ordered_dict2['b'] = 32
print('after adding items again:')
print(ordered_dict)
print(ordered_dict2)
