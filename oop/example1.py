import math
from decimal import Decimal


class Line:
    def __init__(self, coord1, coord2):
        self.coord1_x1, self.coord1_y1 = coord1
        self.coord2_x2, self.coord2_y2 = coord2

    def distance(self):
        return math.sqrt((self.coord2_x2 - self.coord1_x1) ** 2 + (self.coord2_y2 - self.coord1_y1) ** 2)

    def slope(self):
        return (self.coord2_y2 - self.coord1_y1)  / (self.coord2_x2 - self.coord1_x1)

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

coordinate1 = (3,2)
coordinate2 = (8,10)
line1 = Line(coordinate1, coordinate2)
line1_distance = line1.distance()
print(f'line 1 distance: {line1_distance}')
line1_slope = line1.slope()
print(f'line 1 slope: {line1_slope}')

cylinder1 = Cylinder(2, 3)
cylinder1_volume = cylinder1.volume()
print(f'cylinder1 volume: {cylinder1_volume}')
cylinder1_area = cylinder1.surface_area()
print(f'cylinder1 area: {cylinder1_area}')

class Account:
    def __init__(self, owner: str, balance: Decimal = 0):
        self.__owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    def deposit(self, amount: Decimal):
        self.__balance += amount
        print(f'${amount} - Deposit Accepted!')

    def withdraw(self, amount: Decimal):
        if amount > self.__balance:
            print('Funds Unavailable!')
            return

        self.__balance -= amount
        print(f'${amount} - Withdraw Accepted!')

    def __str__(self):
        return f'Owner: {self.__owner}, Balance: {self.__balance}'

account1 = Account('Bob', Decimal(100))
print(account1)
print(f'account owner: {account1.owner}')
print(f'account balance: {account1.balance}')
account1.deposit(Decimal(50.25))
print(f'account balance: {account1.balance}')
account1.withdraw(Decimal(75))
print(f'account balance: {account1.balance}')
account1.withdraw(Decimal(500))
print(f'account balance: {account1.balance}')

