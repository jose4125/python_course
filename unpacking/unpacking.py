values1 = 1,2,3 # This is a tuple
print(f'Original values: {values1}')
print(type(values1))

# Unpacking a tuple
print('Unpacking a tuple', *values1)

# Unpacking tuple into individual variables
value1, value2, value3 = values1
print(f'Original values: {value1}, {value2}, {value3}')

# Unpacking omitting some values
values2 = 4, 5, 6, 7, 8
print(f'Original partial values: {values2}')
value4, _, _, value7, _ = values2
print(f'Value4: {value4}, Value7: {value7}')

# Unpacking omitting the rest values in the middle using *_ and the last value8 -> omitting middle values(value5 and value6)
value4, *_, value7, _ = values2
print(f'Value4: {value4}, Value7: {value7}')

# Unpacking with asterisk to capture remaining values
values3 = 9,10,11,12,13,14
print(f'Original extended values: {values3}')
value9, value10, *rest = values3
print(f'Value9: {value9}, Value10: {value10}, Rest: {rest}')

# Unpacking with asterisk in the middle
value9, value10, *rest, value14 = values3
print(f'Value9: {value9}, Value10: {value10}, Value14: {value14} Rest: {rest}')
print(type(rest))



# Unpacking a list
list1 = [15,16,17,18,19,20]
value15, value16, *rest, value20 = list1
print(f'Value15: {value15}, Value16: {value16}, Value20: {value20} Rest: {rest}')
print(type(rest))



# Unpacking a string
string1 = 'ABCDE'
char1, char2, *rest, char5 = string1
print(f'Char1: {char1}, Char2: {char2}, Char5: {char5} Rest: {rest}')



# Unpacking a set
set1 = {'X', 'Y', 'Z', 'W'}
elem1, elem2, *rest = set1
print(f'Elem1: {elem1}, Elem2: {elem2}, Rest: {rest}')
print(type(rest))



# Unpacking a dictionary (unpacking keys)
dictionary1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
key1, key2, *rest = dictionary1
print(f'Key1: {key1}, Key2: {key2}, Rest: {rest}')
print(type(rest))

# Unpacking a dictionary (unpacking values)
value1, value2, *rest = dictionary1.values()
print(f'Value1: {value1}, Value2: {value2}, Rest: {rest}')
print(type(rest))

# Unpacking a dictionary (unpacking items)
item1, item2, *rest = dictionary1.items()
print(f'Item1: {item1}, Item2: {item2}, Rest: {rest}')
print(type(rest))



# Unpacking nested structures
nested_values = (1, 2, (3, 4, 5), [6, 7, 8])
a, b, (c, *rest_tuple), [d, *rest_list] = nested_values
print(f'a: {a}, b: {b}, c: {c}, rest_tuple: {rest_tuple}, d: {d}, rest_list: {rest_list}')

