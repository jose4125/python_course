from os import path

from snack_machine_project.snack import Snack


class SnackService:
    FILE_NAME = 'snacks.txt'

    def __init__(self):
        self.__snacks_list: list[Snack] = []

        if path.isfile(self.FILE_NAME):
            self.__snacks_list = self.read_snacks()
            return

        self.add_initial_snacks()

    @property
    def snacks_list(self):
        return self.__snacks_list

    @snacks_list.setter
    def snacks_list(self, snacks: list[Snack]):
        self.__snacks_list = snacks


    def read_snacks(self):
        snacks = []
        try:
            with open(self.FILE_NAME, 'r', encoding='utf=8') as file:
                for line in file:
                    snack_info = line.strip().split(',')
                    snack = Snack(snack_info[1], float(snack_info[2]))
                    snacks.append(snack)

            return snacks

        except Exception as e:
            print(f'Error reading the file: {self.FILE_NAME} - Error: {e}')

    def add_initial_snacks(self):
        initial_snacks = [
            Snack('Papas', 70),
            Snack('Chocorramo', 23.05),
            Snack('Tostacos', 34.55)
        ]
        self.snacks_list = initial_snacks
        self.write_snacks(initial_snacks)

    def write_snacks(self, snacks: list[Snack]):
        try:
            with open(self.FILE_NAME, 'a', encoding = 'utf-8') as file:
                for snack in snacks:
                    file.write(f'{snack.write_snack()}\n')
        except Exception as e:
            print(f'Error writing file: {self.FILE_NAME} - Error: {e}')

    def add_snack(self, snack: Snack):
       self.snacks_list.append(snack)
       self.write_snacks([snack])

    def show_snacks(self):
        print('=== Snacks Stock ===')
        for snack in self.snacks_list:
            print(snack)


