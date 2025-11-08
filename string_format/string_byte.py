str_byte1 = b'Hello, World!'
print(str_byte1)  # Output: b'Hello, World!'

str_byte2 = b'Hello, World!'
print(str_byte2[0])  # Output: 72 (ASCII value of 'H')
print(chr(str_byte1[0])) # Output: 'H'

str_byte2_list = str_byte2.split()
print(str_byte2_list) # Output: [b'Hello,', b'World!']


# Converting string to bytes
string1 = 'Hello, World!'
print('string1:', string1)

bytes1 = string1.encode('utf-8')
print('byte encoded:', bytes1)

# Converting bytes to string
byte_to_str = bytes1.decode('utf-8')
print('byte decoded:', byte_to_str)
print('Is byte decoded equal to string1?', byte_to_str == string1)