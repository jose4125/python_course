from collections import defaultdict

default_dict = defaultdict(lambda: 'error, no value found for this key')
default_dict['name'] = 'Alice'
default_dict['age'] = 30

print(f"name: {default_dict['name']} - age: {default_dict['age']}")
print(f'items: {default_dict.items()}')
print(f"address: {default_dict['address']}")

# Defaultdict with list as default factory
default_dict_list = defaultdict(list)

# if key does not exist, it will create an empty list
default_dict_list['fruits']
print(f'items: {default_dict_list}')
default_dict_list['fruits'].append('apple')
default_dict_list['fruits'].append('watermelon')
print(f'list of fruits: {default_dict_list}')
print(f'items of fruits: {default_dict_list.items()}')
print(f'keys of fruits: {default_dict_list.keys()}')
print(f'values of fruits: {default_dict_list.values()}')
