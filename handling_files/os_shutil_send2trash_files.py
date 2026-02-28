import os
import pwd
import shutil
import send2trash

print('=== pwd', pwd)
print('=== os getcwd', os.getcwd())
print('=== dir list', os.listdir())
print('=== projects dir list', os.listdir('/Users/jlombana/Projects'))

path = '/Users/jlombana/Projects/python_course/project_movies'
for folder, sub_folders, files in os.walk(path):
    print(f'Currenty looking at {folder}')
    print('\n')
    print('the subfolders are:')

    for sub_fold in sub_folders:
        print(f'\t Subfolders: {sub_fold}')
    print('\n')
    print('the files are:')
    for file in files:
        print(f'\t File: {file}')
    print('\n')


send2trash.send2trash('remove_file.txt')

shutil.move('test_move.txt', '/Users/jlombana/Projects')
