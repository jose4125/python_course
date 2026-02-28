import shutil
import os
import re

shutil.unpack_archive('unzip_me_for_instructions.zip', 'unziped_folder', 'zip')

with open('./unziped_folder/extracted_content/Instructions.txt', 'r', encoding='utf-8') as file:
    print(file.read())

result = []
pattern = r'\d{3}-\d{3}-\d{4}'
print('pwd', os.getcwd())
path = f'{os.getcwd()}/unziped_folder/extracted_content'
for folder, sub_folders, files in os.walk(path):
    # print('folder', folder)
    for file in files:
        # print('file', file)
        file_path = f'{folder}/{file}'
        # print('file path', file_path)
        with open(file_path, 'r', encoding='utf-8') as textfile:
            content = textfile.read()
            phone_numbers = re.findall(pattern, content)
            if len(phone_numbers):
                for phone_number in phone_numbers:
                    result.append(phone_number)

print('phone numbers', result)