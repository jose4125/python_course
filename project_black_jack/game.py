from project_black_jack.chip import Chip
from project_black_jack.deck import Deck
from project_black_jack.hand import Hand


def take_bet(chip: Chip):
    while True:
        try:
            chip.bet = int(input('How many chips would you like to bet: '))
        except:
            print('Sorry please provide an integer')
        else:
            if chip.bet > chip.total:
                print(f'Sorry, you do not have enough chips! You have: {chip.total}')
            else:
                break

def hit(deck: Deck, hand: Hand):
    card = deck.deal_one()
    hand.add_card(card)

    if card.rank == 'Ace' or hand.aces:
        hand.adjust_for_ace()

def hit_or_stand(deck: Deck, hand: Hand):
    while True:
        hit_or_stand_choice = input('Hit or stand? Enter "h" or "s": ')

        if hit_or_stand_choice[0].lower() == 'h':
            hit(deck, hand)
            return True

        if hit_or_stand_choice[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            return False

        if hit_or_stand_choice[0].lower() != 's' and hit_or_stand_choice[0] != 'h':
            print('Sorry, I did not understand that, Please enter h or s only!')
            continue

        break

def show_some(player: Hand, dealer: Hand):
    print("Dealer's Hand: ")
    print('First card Hidden!')
    print(dealer.cards[1])

    print("Player's Hand")
    for card in player.cards:
        print(card)

    print(f"Value of Player's hand is {player.value}")

def show_all(player: Hand, dealer: Hand):
    print("Dealer's Hand")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is {dealer.value}")

    print("Player's Hand")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is {player.value}")

def player_busts(chips: Chip):
    print('Bust Player!')
    chips.lose_bet()

def player_wins(chips: Chip):
    print('Player Wins!')
    chips.win_bet()

def dealer_busts(chips: Chip):
    print('Player Wins! Dealer Busted')
    chips.win_bet()

def dealer_wins(chips: Chip):
    print('Dealer Wins!')
    chips.lose_bet()

def push():
    print('Dealer and Player tie! PUSH')

def play_game():
    playing = True
    while True:
        print('Welcome to Blackjack')
        # Create and shuffle the deck, deal two cards to each player
        new_deck = Deck()
        new_deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(new_deck.deal_one())
        player_hand.add_card(new_deck.deal_one())

        dealer_hand = Hand()
        dealer_hand.add_card(new_deck.deal_one())
        dealer_hand.add_card(new_deck.deal_one())

        # set up player's chips
        player_chips = Chip()

        # prompt the player for their bet
        take_bet(player_chips)

        # show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:
            # prompt player to hit or stand
            playing = hit_or_stand(new_deck, player_hand)

            # show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # if player's hand exceeds 21, run player_bust() and break out of loop
            print(f"Player hand's value {player_hand.value}")
            if player_hand.value > 21:
                player_busts(player_chips)
                break

        # if player hasn't busted, play Dealer's hand until dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(new_deck, dealer_hand)

            # show all cards
            show_all(player_hand, dealer_hand)

            # run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
            else:
                push()

        print(f'Player total chips are at: {player_chips.total}')

        # ask play again
        new_game = input('Do you want to play again? [y/n]')

        if new_game[0].lower() == 'y':
            playing = True
            continue





play_game()