# with - handle it context manager
# with - open and close file automatically
# don't need the try - except - finally block

# __enter__ invoked when the execution flow enters the context of the with statement and opens the file
#__exit__ invoked when the execution flow leaves the context of the with statement and closes the file
with open('text_file.txt', 'r', encoding='utf-8') as file:
    print(file.read())
