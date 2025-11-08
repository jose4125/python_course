numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'numbers: {numbers}')

squares_map= map(lambda num: num ** 2, numbers)
print(f'squares map: {squares_map}')

squares_list = list(squares_map)
print(f'squares list: {squares_list}')