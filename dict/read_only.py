from types import MappingProxyType

dict = {'one': 1, 'two': 2, 'three': 3}
read_only_dict = MappingProxyType(dict)

print(f'read only dict: {read_only_dict}')
print(f'value for "two": {read_only_dict["two"]}')

# Modifying the original dictionary will reflect in the read-only view
dict['two'] = 22
print(f'dict: {dict}')
print(f'read only dict: {read_only_dict}')
