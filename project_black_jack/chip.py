class Chip:
    def __init__(self, total=100):
        self.__total = total
        self.__bet = 0

    @property
    def bet(self):
        return self.__bet

    @bet.setter
    def bet(self, amount: int):
        self.__bet = amount

    @property
    def total(self):
        return self.__total

    def win_bet(self):
        self.__total += self.__bet

    def lose_bet(self):
        self.__total -= self.__bet
