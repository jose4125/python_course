numbers = [1,2,3,4,5,6,7,8,9,10]

pairs_numbers_filter = filter(lambda num: num % 2 == 0, numbers)
print(f'pairs number filter {pairs_numbers_filter}')

pairs_numbers_list = list(pairs_numbers_filter)
print(f'pairs number list {pairs_numbers_list}')