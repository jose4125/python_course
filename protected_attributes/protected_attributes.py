class Libro:
    def __init__(self, titulo: str, autor: str, genero:str):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def genero(self):
        return self.__genero

class Biblioteca:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__libros: list[Libro] = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def libros(self):
        return self.__libros

    def agregar_libro(self, libro: Libro):
        self.__libros.append(libro)

    def buscar_libro_por_autor(self, autor: str):
        return [self.mostrar_libro(libro) for libro in self.__libros if autor.lower() == libro.autor.lower()]

    def buscar_libro_por_genero(self, genero: str):
        return [self.mostrar_libro(libro) for libro in self.__libros if genero.lower() == libro.genero.lower()]

    def listar_libros(self):
        for libro in self.__libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self, libro: Libro):
        return f'Título: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}'

biblioteca_nacional = Biblioteca('Biblioteca Nacional')
print(f'Bienvenidos a la {biblioteca_nacional.nombre}')
libro1 = Libro('Cien Años de Soledad', 'Gabriel García Márquez', 'Realismo Mágico')
libro2 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Novela')
libro3 = Libro('La Sombra del Viento', 'Carlos Ruiz Zafón', 'Misterio')
libro4 = Libro('La Ciudad y los Perros', 'Mario Vargas Llosa', 'Novela')
libro5 = Libro('Conversación en La Catedral', 'Mario Vargas Llosa', 'Novela')

biblioteca_nacional.agregar_libro(libro1)
biblioteca_nacional.agregar_libro(libro2)
biblioteca_nacional.agregar_libro(libro3)
biblioteca_nacional.agregar_libro(libro4)
biblioteca_nacional.agregar_libro(libro5)

autor = 'Mario Vargas Llosa'
print(f'\nLibros del autor {autor}:')
biblioteca_nacional.buscar_libro_por_autor(autor)