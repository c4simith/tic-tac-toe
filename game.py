from gameops import load_gameinstructions, init_players, get_playerinput, display_gameboard, is_winningmove

valid_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
position_map = {"1": (2, 0), "2": (2, 1), "3": (2, 2),
                "4": (1, 0), "5": (1, 1), "6": (1, 2),
                "7": (0, 0), "8": (0, 1), "9": (0, 2)}
board_elements = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
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

    marking_position = get_playerinput(board_elements, current_player, position_map, valid_positions)
    x, y = position_map.get(marking_position)
    board_elements[x][y] = marking_symbol
    display_gameboard(board_elements)
    if is_winningmove(board_elements, marking_symbol):
        winner = current_player
        break

if winner == "":
    print("Game ended in a tie!!")
else:
    print(f"Player {winner} won the game!!")
