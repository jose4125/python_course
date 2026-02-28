from typing import List

from project_war_game.card import Card


class Player:
    def __init__(self, name: str):
        self.__name = name
        self.__deck = []

    @property
    def deck(self):
        return self.__deck

    def remove_one(self) -> Card:
        return self.__deck.pop(0)

    def add_cards(self, new_cards: Card | List[Card]):
        if type(new_cards) == type([]):
            return self.__deck.extend(new_cards)

        return self.__deck.append(new_cards)


    def __str__(self):
        return f'Player {self.__name} has {len(self.__deck)} cards'

if __name__ == '__main__':
    card_1 = Card('Clubs', 'Four')
    player_1 = Player('Player 1')
    print(player_1)
    player_1.add_cards([card_1])
    print(player_1)
    print(card_1)
    print(player_1.deck[0])

