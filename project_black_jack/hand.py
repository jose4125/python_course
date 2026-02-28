from project_black_jack.card import Card


class Hand:
    def __init__(self,):
        self.__cards = []
        self.__value = 0
        self.__aces = 0

    @property
    def cards(self):
        return self.__cards

    @property
    def value(self):
        return self.__value

    @property
    def aces(self):
        return self.__aces

    def add_card(self, card: Card):
        print(f'adding card: ', card)
        print(f'Current value: {self.__value}')

        self.__cards.append(card)
        self.__value += card.value
        print(f'New value: {self.__value}')

        if card.rank == 'Ace':
            self.__aces += 1

    def adjust_for_ace(self):
        while self.__value > 21 and self.__aces:
            self.__value -= 10
            self.__aces -= 1

if __name__ == '__main__':
    test_player = Hand()
    pulled_card = Card('Clubs', 'Ace')
    print(pulled_card)
    test_player.add_card(pulled_card)
    print(test_player.value)
    pulled_card = Card('Spades', 'Ace')
    print(pulled_card)
    test_player.add_card(pulled_card)
    print(test_player.value)
    test_player.adjust_for_ace()
    print(test_player.value)

    pulled_card = Card('Spades', 'Nine')
    print(pulled_card)
    test_player.add_card(pulled_card)
    print(test_player.value)
    test_player.adjust_for_ace()
    print(test_player.value)
