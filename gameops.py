def display_gameboard(board_elements):
    for row in board_elements:
        print(f"|\t{row[0]}\t|\t{row[1]}\t|\t{row[2]} \t|")
        print()


def load_gameinstructions():
    print("TIC-TAC-TOE GAME")
    print("---------------------------------------------------")
    print("How to play :\n"
          "Current player have to input a postion between 1-9.\n"
          "The X or O will be marked to respective postion.\n"
          "Starting player gets X symbol.\n")
    print("Postion marking:")
    display_gameboard([["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]])
    print("---------------------------------------------------")


def init_players():
    player1 = input("Enter a name for player 1 : ")
    if player1 == "":
        player1 = "Player1"

    player2 = input("Enter a name for player 2 : ")
    if player2 == "":
        player2 = "Player2"
    if player2 == player1:
        player2 = player2 + "_2"

    return player1, player2


def get_playerinput(board_elements, current_player, position_map, valid_positions):
    while True:
        player_entry = input(f"Next move is for {current_player}. Enter position : ")
        if player_entry in valid_positions:
            x, y = position_map.get(player_entry)
            if board_elements[x][y] != " ":
                print("Invalid position. Postion already marked")
            else:
                return player_entry
        else:
            print("Invalid position. Expected 1-9")


def is_winningmove(board_elements, marking_symbol):
    for i in [0, 1, 2]:
        if board_elements[i][0] == board_elements[i][1] == board_elements[i][2] == marking_symbol:
            return True
    for j in [0, 1, 2]:
        if board_elements[0][j] == board_elements[1][j] == board_elements[2][j] == marking_symbol:
            return True
    if board_elements[0][0] == board_elements[1][1] == board_elements[2][2] == marking_symbol:
        return True
    if board_elements[2][0] == board_elements[1][1] == board_elements[0][2] == marking_symbol:
        return True
    return False
