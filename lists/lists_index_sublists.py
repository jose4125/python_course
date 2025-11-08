numbers1 = [1, 2, 3, 4, 5, 6]
# get the index of the first occurrence of 4
index4 = numbers1.index(4)
print(f'index of number 4: {index4}')

# get the elements from 2 to 4 (not including 4)
sublist1 = numbers1[1:3]
print(f'sublist from index 1 to 3: {sublist1}')

# get the elements from the beginning to index 5 (not including 5)
sublist2 = numbers1[:4]
print(f'sublist from beginning to index 4: {sublist2}')

# get the elements from index 3 to the end
sublist3 = numbers1[3:]
print(f'sublist from index 3 to the end: {sublist3}')

# get the elements with step 2
sublist4 = numbers1[::2]
print(f'sublist with step 2: {sublist4}')

# get last element
sublist5 = numbers1[-1]
print(f'last element: {sublist5}')

# get elements from index -4 to -1 (not including -1)
sublist6 = numbers1[-4:-1]
print(f'sublist from index -4 to -1: {sublist6}')

# get last 2 elements
sublist7 = numbers1[-2:]
print(f'last 2 elements: {sublist7}')

# get last 3 elements
sublist8 = numbers1[-3:]
print(f'last 3 elements: {sublist8}')
