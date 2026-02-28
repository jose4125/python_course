from random import shuffle
from typing import List

from project_black_jack.card import suits, ranks, Card


class Deck:
    def __init__(self):
        self.__deck: List[Card] = []
        for suit in suits:
            for rank in ranks:
                self.__deck.append(Card(suit, rank))

    @property
    def deck(self):
        return self.__deck

    def shuffle(self):
        shuffle(self.__deck)

    def deal_one(self):
        return self.__deck.pop()

if __name__ == '__main__':
    deck1 = Deck()
    print(deck1.deck[-1])
    deck1.shuffle()
    print(deck1.deck[-1])
