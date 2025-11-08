from os import remove

from Movies_project.domain.movie import Movie


class MovieCatalog:
    file_path: str = 'movies.txt'

    @classmethod
    def add_movie(cls, movie: Movie):
        with open(cls.file_path, 'a', encoding='utf-8') as file:
            file.write(f'{movie.title}\n' )

    @classmethod
    def list_catalog(cls):
        with open(cls.file_path, 'r', encoding='utf=8') as file:
            print('Movie Catalog:'.center(50, '-'))
            print(file.read())

    @classmethod
    def remove_catalog(cls):
        remove(cls.file_path)
        print(f'The movie catalog {cls.file_path} has been removed.')


