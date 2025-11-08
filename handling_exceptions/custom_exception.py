class CustomError(Exception):
    def __init__(self, message: str):
        # this message attribute comes from the parent class Exception
        self.message = message