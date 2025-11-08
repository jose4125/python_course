try:
    file = open('text_file.txt', 'r', encoding='utf-8')

    # read all lines into a list
    print(file.readlines())
finally:
    file.close()

