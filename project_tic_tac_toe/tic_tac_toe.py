board_game = [' ' for _ in range(9)]
def clear_output():
    print('\n'*100)

def display_board(board):
    clear_output()
    board_lines = ''
    for index, item in enumerate(board):
        print('index:', index)
        if((index + 1) % 3 != 0):
            board_lines += f' {board[index]} |'

        if ((index + 1) % 3 == 0):
            print('end of row')
            board_lines += f' {board[index]}\n---+----+---\n'
    print(board_lines)

def choose_player_marker():
    marker = ''

    while marker not in ['X', 'O']:
        marker = input('Player1, choose X or O: ').upper()

    player1 = marker.upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f'Player 1 chosen: {player1} | Player 2 chosen: {player2}')
    return player1, player2

def user_choice(player, player_turn):
    is_valid = False
    position = 0

    while not is_valid:
        position = input(f"Player {player}({player_turn}), please enter your choice (1-9): ")

        if position.isdigit() and 1 <= int(position) <= 9:
            is_valid = True

        if position.isdigit() and int(position) < 1 or int(position) > 9:
            print("Please enter a number within the range of 1-9.")

        if not position.isdigit():
            print("Sorry that is not a digit.")

    return int(position) - 1

# 123, 456, 789
# 147, 258, 369
# 159, 357
def check_winner(board, player_marker):
    return ((board[0] == board[1] == board[2] == player_marker) or
            (board[3] == board[4] == board[5] == player_marker) or
            (board[6] == board[7] == board[8] == player_marker) or
            (board[0] == board[3] == board[6] == player_marker) or
            (board[1] == board[4] == board[7] == player_marker) or
            (board[2] == board[5] == board[8] == player_marker) or
            (board[0] == board[4] == board[8] == player_marker) or
            (board[2] == board[4] == board[6] == player_marker))


def place_marker(board, marker, position):
    board[position] = marker


def change_player(player_turn, player):
    if player_turn == player1_marker:
        print('change to player 2')
        player_turn = player2_marker
        player += 1
    else:
        print('change to player 1')
        player_turn = player1_marker
        player -= 1

    return player_turn, player


def star(board):
    end_game = False
    player_marker = player1_marker
    player = 1

    while not end_game:
        if ' ' not in board:
            break

        position = user_choice(player, player_marker)

        if board[position] == ' ':
            place_marker(board, player_marker, position)
            has_winner = check_winner(board, player_marker)

            if  not has_winner:
                player_marker, player =  change_player(player_marker, player)
            else:
                end_game = True

            display_board(board)
        else:
            print(f'Position {position} is already taken.')

    if end_game:
        print(f'Player {player} wins!')
    else:
        print('No winner, it"s a tie')


display_board(board_game)
player1_marker, player2_marker = choose_player_marker()
star(board_game)

