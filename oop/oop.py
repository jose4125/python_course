class DispositivoEntrada:
    def __init__(self, marca:str, tipo_entrada:str):
        self.__marca = marca
        self.__tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self.__marca

    @property
    def tipo_entrada(self):
        return self.__tipo_entrada

    @marca.setter
    def marca(self, marca:str):
        self.__marca = marca

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada:str):
        self.__tipo_entrada = tipo_entrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca: str, tipo_entrada: str):
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones += 1
        self.__raton_id = Raton.contador_ratones

    def __str__(self):
        return f'Raton [ID: {self.__raton_id}, Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}]'

class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, marca:str, tipo_entrada:str):
        super().__init__(marca, tipo_entrada)
        Teclado.contador_teclado += 1
        self.__teclado_id = Teclado.contador_teclado

    def __str__(self):
        return f'Teclado [ID: {self.__teclado_id}, Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}]'

class Monitor:
    contador_monitor = 0

    def __init__(self, marca:str, tamano:int):
        Monitor.contador_monitor += 1
        self.__monitor_id = Monitor.contador_monitor
        self.__marca = marca
        self.__tamano = tamano

    def __str__(self):
        return f'Monitor [ID: {self.__monitor_id}, Marca: {self.__marca}, Tamaño: {self.__tamano}]'

class Computadora:
    contador_computadora = 0

    def __init__(self, nombre:str, monitor: Monitor, teclado: Teclado, raton: Raton):
        Computadora.contador_computadora += 1
        self.__computador_id = Computadora.contador_computadora
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    def __str__(self):
        return (f'''Computadora [ID: {self.__computador_id} 
                Nombre: {self.__nombre}
                Monitor:  {self.__monitor}
                Teclado: {self.__teclado}
                Raton:  {self.__raton}]''')

class Orden:
    contador_orden = 0

    def __init__(self, computadoras: list[Computadora]):
        Orden.contador_orden += 1
        self.__orden_id = Orden.contador_orden
        self.__computadoras = computadoras


    def agregar_computadora(self, computadora: Computadora):
        self.__computadoras.append(computadora)

    def __str__(self):
        computadoras_str = '\n'.join([str(computadora) for computadora in self.__computadoras])
        return f'Orden [ID: {self.__orden_id}]\nComputadoras:\n{computadoras_str}'



# print the MRO - Method Resolution Order.
print(f'MRO method: {Raton.mro()}')
print(f'MRO dunder: {Raton.__mro__}')


raton1 = Raton('HP', 'USB')
print(raton1)

raton2 = Raton('Acer', 'Bluetooth')
print(raton2)

teclado1 = Teclado('HP', 'USB')
print(teclado1)
teclado2 = Teclado('DELL', 'Bluetooth')
print(teclado2)

monitor1 = Monitor('HP', 15)
print(monitor1)
monitor2 = Monitor('Acer', 27)
print(monitor2)

computadora1 = Computadora('HP', monitor1, teclado1, raton1)
print(computadora1)
computadora2 = Computadora('DELL', monitor2, teclado2, raton2)
print(computadora2)

orden1 = Orden([computadora1])
print(orden1)
orden2 = Orden([computadora2, computadora1])
print(orden2)