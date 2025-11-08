try:
    file = open('text_file.txt', 'r', encoding='utf-8')

    # read specific line
    print(file.readlines()[1])
finally:
    file.close()
