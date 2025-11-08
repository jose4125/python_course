from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho: float, alto: float):
        if self.__validar_valor(ancho):
            self.__ancho = ancho
        else:
            self.__ancho = 0
            print('Error: El ancho deben estar entre 0 y 10.')

        if self.__validar_valor(alto):
            self.__alto = alto
        else:
            self.__alto = 0
            print('Error: El alto deben estar entre 0 y 10.')

    @property
    def ancho(self):
        return self.__ancho

    @property
    def alto(self):
        return self.__alto

    @ancho.setter
    def ancho(self, ancho: float):
        if self.__validar_valor(ancho):
            self.__ancho = ancho
        else:
            print('Error: El ancho deben estar entre 0 y 10.')


    @alto.setter
    def alto(self, alto: float):
        if self.__validar_valor(alto):
            self.__alto = alto
        else:
            print('Error: El alto deben estar entre 0 y 10.')

    def __validar_valor(self, valor: float):
        return True if 0 < valor > 10 else False

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self.__ancho}, Alto: {self.__alto}]'

class Color:
    def __init__(self, color: str):
        self.__color = color

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, color: str):
        self.__color = color

    def __str__(self):
        return f'Color [Color: {self.__color}]'

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado: float, color: str):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho: float, alto:float, color: str):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


cuadrado1 = Cuadrado(5, 'rojo')
print(f'calculo area cuadrado: {cuadrado1.area()}')

rectangulo1 = Rectangulo(3, 8, 'verde')
print(f'calculo area rectangulo: {rectangulo1.area()}')
print(rectangulo1)