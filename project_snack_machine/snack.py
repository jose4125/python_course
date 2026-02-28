class Snack:
    __snack_count = 0

    def __init__(self, name: str, price: int | float):
        Snack.__snack_count += 1
        self.__snack_id = Snack.__snack_count
        self.__name = name
        self.__price = round(float(price), 2)

    @property
    def snack_id(self):
        return self.__snack_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: int | float):
        self.__price = round(float(price), 2)

    def write_snack(self):
        return f'{self.__snack_id},{self.__name},{self.__price}'

    def __str__(self):
        return f'snack id: {self.__snack_id}, name: {self.__name}, price: {self.__price:.2f}'

