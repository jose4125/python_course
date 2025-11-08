try:
    file = open('text_file.txt', 'r', encoding='utf-8')
    # iterate through the file object
    for line in file:
        print(line.strip())  # strip() to remove leading/trailing whitespace
finally:
    file.close()