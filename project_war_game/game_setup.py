from project_war_game.deck import Deck
from project_war_game.player import Player

player_1 = Player('Player 1')
player_2 = Player('Player 2')
new_deck = Deck()
new_deck.shuffle()

for index in range(26):
    player_1.add_cards(new_deck.deal_one())
    player_2.add_cards(new_deck.deal_one())
print('Playe 1 deck:', len(player_1.deck))
print('Player 2 deck:', len(player_2.deck))

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Round #{round_num}')
    print('Player 1 deck:', len(player_1.deck))
    print('Player 2 deck:', len(player_2.deck))

    if len(player_1.deck) == 0:
        print('Player 1, out of cards! Player 2 wins')
        game_on = False
        break

    if len(player_2.deck) == 0:
        print('Player 2, out of cards! Player 1 wins')
        game_on = False
        break

    player_1_cards_in_game = [player_1.remove_one()]
    player_2_cards_in_game = [player_2.remove_one()]

    if player_1_cards_in_game[0].value > player_2_cards_in_game[0].value:
        player_1_cards_in_game.extend(player_2_cards_in_game)
        player_1.add_cards(player_1_cards_in_game)

    if player_2_cards_in_game[0].value > player_1_cards_in_game[0].value:
        player_2_cards_in_game.extend(player_1_cards_in_game)
        player_2.add_cards(player_2_cards_in_game)

    at_war = player_1_cards_in_game[0].value == player_2_cards_in_game[0].value

    while at_war:
        print('At War!!!')
        if len(player_1.deck) < 4:
            print('Player 1, out of cards! Player 2 wins')
            at_war = False
            game_on = False
            break

        if len(player_2.deck) < 4:
            print('Player 1, out of cards! Player 2 wins')
            at_war = False
            game_on = False
            break

        for index in range(4):
            player_1_cards_in_game.append(player_1.remove_one())
            player_2_cards_in_game.append(player_2.remove_one())

        if player_1_cards_in_game[-1].value > player_2_cards_in_game[-1].value:
            player_1_cards_in_game.extend(player_2_cards_in_game)
            player_1.add_cards(player_1_cards_in_game)
            at_war = False

        if player_2_cards_in_game[-1].value > player_1_cards_in_game[-1].value:
            player_2_cards_in_game.extend(player_1_cards_in_game)
            player_2.add_cards(player_2_cards_in_game)
            at_war = False


