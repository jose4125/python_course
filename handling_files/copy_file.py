try:
    file = open('text_file.txt', 'r', encoding='utf-8')

    # copy content to another file
    # 'a' mode is used to append content to the file if it already exists
    # 'w' mode can also be used to overwrite the file
    copy_file = open('copy_file.txt', 'a', encoding='utf-8')
    copy_file.write(file.read())
finally:
    file.close()
    copy_file.close()
    print('had finished reading and copying file')