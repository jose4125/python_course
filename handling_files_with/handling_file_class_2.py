from handling_files_with.handlig_file_class import HandlingFile

with HandlingFile('text_file.txt') as file:
    print(file.read())