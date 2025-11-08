try:
    file = open('text_file.txt', 'r', encoding='utf-8')

    # read some content, read 3 characters
    print(file.read(3))
    print(file.read(3))

    # read line
    print(file.readline())

    # read the rest of the content or the whole file
    print(file.read())
finally:
    file.close()