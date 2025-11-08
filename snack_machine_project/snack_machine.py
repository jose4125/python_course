from snack_machine_project.snack import Snack
from snack_machine_project.snack_service import SnackService


class SnacksMachine:
    def __init__(self, snack_service: SnackService):
        self.__snack_service = snack_service
        self.__shopping_cart = []

    def snack_machine(self):
        exit_machine = False
        print('*** Snack Machine ***')

        self.__snack_service.show_snacks()

        while not exit_machine:
            try:
                option = self.__show_menu()
                exit_machine = self.__run_option(option)
            except Exception as e:
                print(f' Error: {e}')

    def __show_menu(self):
        print('''
        Menu:
        1. add snack to the shopping cart
        2. show ticket
        3. add snack to the stock
        4. show all snacks
        5. exit
        ''')

        return int(input('Select an option: '))

    def __run_option(self, option: int):
        if option == 1:
            self.__add_snack_to_shopping_cart()
            return False

        if option == 2:
            self.__show_ticket()
            return False

        if option == 3:
            self.__add_snack_to_stock()
            return False

        if option == 4:
            self.__list_snacks()
            return False

        if option == 5:
            print('Exiting..., Come back soon')
            exit_machine = True
            return exit_machine

        if option < 1 or option > 5:
            print(f'Invalid option: {option}')
            return False

        return False

    def __add_snack_to_shopping_cart(self):
        snack_id = int(input('Enter the snack id: '))
        snacks = self.__snack_service.snacks_list
        snack = next((snack for snack in snacks if snack.snack_id == snack_id), None)

        if snack:
            self.__shopping_cart.append(snack)
            print(f'Added {snack.name} to the shopping cart')
            return

        print(f'Snack with id: {snack_id} not found')

    def __show_ticket(self):
        if not self.__shopping_cart:
            print(f'No items founded in the shopping cart')
            return

        total_price = sum(snack.price for snack in self.__shopping_cart)
        print('=== Ticket ===')

        for snack in self.__shopping_cart:
            print(f'\t{snack.name}  - ${snack.price:.2f}')

        print(f'\tTotal price: {total_price:.2f}')

    def __add_snack_to_stock(self):
        snack_name = input('Enter the snack name: ')
        snack_price = float(input('Enter the snack price: '))

        self.__snack_service.add_snack(Snack(snack_name, snack_price))
        print(f'Added {snack_name} to the stock')

    def __list_snacks(self):
        self.__snack_service.show_snacks()


if __name__ == '__main__':
    snack_machine1 = SnacksMachine(SnackService())
    snack_machine1.snack_machine()