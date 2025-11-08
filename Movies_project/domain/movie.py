class Movie:
    def __init__(self, title:str):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    def __str__(self):
        return f'movie: {self.title}'