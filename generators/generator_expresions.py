my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# generator comprehension
gencomp = (item ** 2 for item in my_list if item > 3)

for item in gencomp:
    print(item)