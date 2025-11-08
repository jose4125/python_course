from Movies_project.domain.movie import Movie
from Movies_project.services.movie_catalog import MovieCatalog

menu_option = None

while menu_option != 4:
    try:
        print('Movie Catalog Menu'.center(50, '-'))
        print('1. Add Movie')
        print('2. List Movies')
        print('3. Remove Movie Catalog')
        print('4. Exit')

        menu_option = int(input('Select an option (1-4): '))

        if menu_option == 1:
            movie_title = input('Movie Title: ')
            movie = Movie(movie_title)
            MovieCatalog.add_movie(movie)
            print('Movie Catalog Added'.center(50, '-'))

        if menu_option == 2:
            MovieCatalog.list_catalog()
            print('Movie Catalog Listed'.center(50, '-'))

        if menu_option == 3:
            MovieCatalog.remove_catalog()
            print('Movie Catalog Removed'.center(50, '-'))

        if menu_option == 4:
            print('Exiting the Movie Catalog Menu.')

        if menu_option < 1 or menu_option > 4:
            print('Invalid option. Please select a valid option (1-4).')

    except Exception as e:
        print('Invalid input. Please enter a number between 1 and 4.')
        menu_option = None

else:
    print('Thank you for using the Movie Catalog Menu.')