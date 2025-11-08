# 'x' means exclusive mode
# if the file exist raise an FileExistError, because of the exclusive mode
file_name = 'exist_file.txt'
try:
    with open(file_name, 'x', encoding = 'utf-8') as file:
        file.write('hello world')
        file.write('file already exist')
        print(f'File {file_name} created successfully')

except FileExistsError as e:
    print(f'File {file_name} already exists, error: {e}')
