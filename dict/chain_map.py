# Search in multiple dictionaries using ChainMap
from typing import ChainMap

dict1 = {'one': 1, 'two': 2, 'three': 3}
dict2 = {'four': 4, 'five': 5, 'six': 6}
dict3 = {'seven': 7, 'eight': 8, 'nine': 9}

# Combine dictionaries using ChainMap
merge_dict = ChainMap(dict1, dict2, dict3)
print(f'Merged dict using ChainMap: {merge_dict}')

# Access values from the combined dictionary, (from left to right)
print(f'value for "five": {merge_dict["five"]}')