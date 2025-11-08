# Demonstrating different string formatting techniques in Python


# Using % operator
name1 = 'Alice'
string1 = 'hello %s'%name1
print(string1)

string2 = 'hello %s %s, your score is %d'%('Alice', 'Doe', 95)
print(string2)

employee1 = ('Bob', 'Smith', 30, 60000.50)
message_format1 = 'Employee: %s %s, Age: %d, Salary: %.2f'%employee1
print(message_format1)

employee2 = ('Karl', 'Smith', 23, 60000.500)
message_format2 = 'Employee: %s %s, Age: %d, Salary: %.2f'
print(message_format2%employee2)



# Using format() method
name2 = 'Charlie'
age2 = 28
score2 = 88.756

# Using placeholders
string3 = 'Name: {}, Age: {}, Score: {:.2f}'.format(name2, age2, score2)
print(string3)

# Using positional indices in the placeholders
string4 = 'Name: {0}, Age: {1}, Score: {2:.2f}'.format(name2, age2, score2)
print(string4)

# Reordering the placeholders using positional indices
string5 = 'Score: {2:.2f}, Name: {0}, Age: {1}'.format(name2, age2, score2)
print(string5)

# Using named placeholders
string6 = 'Name: {name}, Age: {age}, Score: {score:.2f}'.format(name = name2, age = age2, score = score2)
print(string6)

# Using dictionary to format string
person1 = {'name': 'David', 'last_name': 'Johnson', 'age': 35, 'score': 750.456}
string7 = 'Name: {person[name]}, Last Name: {person[last_name]}, Age: {person[age]}, Score: {person[score]:.2f}'.format(person = person1)
print(string7)



# Using f-strings (formatted string literals)
string8 = f'Name: {name2}, Age: {age2}, Score: {score2:.2f}'
print(string8)



# scaping characters in strings
path1 = 'C:\\Users\\Alice\\Documents\\file.txt'
print(path1)

# raw strings
# Without raw string
string9 = 'This is a raw string with a newline character: \n and a tab character: \t'
print(string9)

# With raw string - using r prefix to ignore escape sequences
raw_string1 = r'This is a raw string with a newline character: \n and a tab character: \t'
print(raw_string1)

# Using raw string for file paths
path2 = r'C:\Users\Alice\\Documents\file.txt'
print(path2)


# ascii characters
char1 = 'A'
ascii_value1 = ord(char1)
print(f'The ASCII value of {char1} is {ascii_value1}')

ascii_value2 = 66
char2 = chr(ascii_value2)
print(f'The character for ASCII value {ascii_value2} is {char2}')


# strip whitespace
string10 = '   Hello, World!   '
stripped_string1 = string10.strip()
print(f'Original string: "{string10}"')
print(f'Stripped string: "{stripped_string1}"')

# strip specific characters
string11 = '***Hello, World!***'
stripped_string2 = string11.strip('*')
print(f'Original string: "{string11}"')
print(f'Stripped string: "{stripped_string2}"')

# lstrip
string12 = '   Hello, World!   '
lstripped_string = string12.lstrip()
print(f'Original string: "{string12}"')
print(f'LStripped string: "{lstripped_string}"')
# rstrip
string13 = '   Hello, World!   '
rstripped_string = string13.rstrip()
print(f'Original string: "{string13}"')
print(f'RStripped string: "{rstripped_string}"')

string14 = ' *** Hello, World! *** '.strip(' *')
print(f'Original string: " *** Hello, World! *** "')
print(f'Stripped string: "{string14}"')