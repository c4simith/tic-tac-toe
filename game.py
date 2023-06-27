from gameops import load_gameinstructions, init_players, get_playerinput, display_gameboard, is_winningmove

valid_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
board_elements = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " ",}
current_player = ""
marking_symbol = ""
winner = ""

load_gameinstructions()
player1, player2 = init_players()

for i in range(1, 10):
    if i % 2 != 0:
        current_player = player1
        marking_symbol = "X"
    else:
        current_player = player2
        marking_symbol = "O"

    marking_position = get_playerinput(board_elements, current_player, valid_positions)
    board_elements[marking_position] = marking_symbol
    display_gameboard(board_elements)
    if is_winningmove(board_elements, marking_symbol):
        winner = current_player
        break

if winner == "":
    print("Game ended in a tie!!")
else:
    print(f"Player {winner} won the game!!")
