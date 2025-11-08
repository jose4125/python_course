try:
    file = open('text_file.txt', 'r', encoding='utf-8')

    for index, line in enumerate(file, start=1):
        print(f'Line {index}: {line.strip()}')
finally:
    file.close()
