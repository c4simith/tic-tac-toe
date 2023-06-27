def display_gameboard(board_elements):
    print(f'|\t{board_elements["7"]}\t|\t{board_elements["8"]}\t|\t{board_elements["9"]} \t|')
    print()
    print(f'|\t{board_elements["4"]}\t|\t{board_elements["5"]}\t|\t{board_elements["6"]} \t|')
    print()
    print(f'|\t{board_elements["1"]}\t|\t{board_elements["2"]}\t|\t{board_elements["3"]} \t|')
    print()


def load_gameinstructions():
    print("TIC-TAC-TOE GAME")
    print("---------------------------------------------------")
    print("How to play :\n"
          "Current player have to input a postion between 1-9.\n"
          "The X or O will be marked to respective postion.\n"
          "Starting player gets X symbol.\n")
    print("Postion marking:")
    board_elements = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", }
    display_gameboard(board_elements)
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


def get_playerinput(board_elements, current_player, valid_positions):
    while True:
        position = input(f"Next move is for {current_player}. Enter position : ")
        if position in valid_positions:
            if board_elements[position] != " ":
                print("Invalid position. Postion already marked")
            else:
                return position
        else:
            print("Invalid position. Expected 1-9")


def is_winningmove(board_elements, marking_symbol):
    if board_elements["7"] == board_elements["8"] == board_elements["9"] == marking_symbol:
        return True
    if board_elements["4"] == board_elements["5"] == board_elements["6"] == marking_symbol:
        return True
    if board_elements["1"] == board_elements["2"] == board_elements["3"] == marking_symbol:
        return True
    if board_elements["7"] == board_elements["4"] == board_elements["1"] == marking_symbol:
        return True
    if board_elements["8"] == board_elements["5"] == board_elements["2"] == marking_symbol:
        return True
    if board_elements["9"] == board_elements["6"] == board_elements["3"] == marking_symbol:
        return True
    if board_elements["1"] == board_elements["5"] == board_elements["9"] == marking_symbol:
        return True
    if board_elements["7"] == board_elements["5"] == board_elements["3"] == marking_symbol:
        return True
    return False
