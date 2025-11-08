# with - handle it context manager
# with - open and close file automatically
# don't need the try - except - finally block

# __enter__ invoked when the execution flow enters the context of the with statement and opens the file
#__exit__ invoked when the execution flow leaves the context of the with statement and closes the file

class HandlingFile:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        print('opening file'.center(50, '-'))
        self.file = open(self.file_name, 'r', encoding='utf-8')
        return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        if self.file:
            self.file.close()
        print('closing file'.center(50, '-'))
