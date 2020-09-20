game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def check_winner(a_matrix):
    for i in range(0, len(a_matrix)):
        j = 0
        if a_matrix[j][i] == a_matrix[j+1][i] == a_matrix[j+2][i] == 1:
            return "Player 1 won"
        elif a_matrix[j][i] == a_matrix[j+1][i] == a_matrix[j+2][i] == 2:
            return "Player 2 won"
    for i in range(0, len(a_matrix)):
        if 1 in a_matrix[i] and 2 not in a_matrix[i] and 0 not in a_matrix[i]:
            return "Player 1 won"
        elif 1 not in a_matrix[i] and 2 in a_matrix[i] and 0 not in a_matrix[i]:
            return "Player 2 won"
    if a_matrix[0][0] == a_matrix[1][1] == a_matrix[2][2] == 1:
        return "Player 1 won"
    elif a_matrix[0][0] == a_matrix[1][1] == a_matrix[2][2] == 2:
        return "Player 2 won"
    elif a_matrix[0][2] == a_matrix[1][1] == a_matrix[2][0] == 1:
        return "Player 1 won"
    elif a_matrix[0][2] == a_matrix[1][1] == a_matrix[2][0] == 2:
        return "Player 2 won"
    return "No one won"


def display_matrix(data_matrix):
    # for data in data_matrix:
    #     print(data)
    print()
    print(" ---" * 3)
    for data in data_matrix:
        for i in data:
            # print("| {} ".format(data[i]) * 4)
            print("| {} ".format(i), end="")
        print("|")
        print(" ---" * 3)
    print()


def update_matrix(player, row_count, data_matrix):
    player_list = row_count.strip().split(",")
    for row in range(0, len(player_list)):
        player_list[row] = int(player_list[row])

    if data_matrix[player_list[0]-1][player_list[1]-1] == 0:
        data_matrix[player_list[0]-1][player_list[1]-1] = player
        return True
    else:
        print("Place already Taken !!!")
        return False


def space_available(data_matrix):
    for data in data_matrix:
        if 0 in data:
            return True
    return False


if __name__ == "__main__":
    display_matrix(game_board)
    updated = False
    result = ""
    while "Player" not in result:
        if not space_available(game_board):
            print("All options out, No one won !!!")
            break
        while not updated:
            player1 = input("Player 1 - Enter the row[1-3], column[1-3] : ")
            updated = update_matrix(1, player1, game_board)
        display_matrix(game_board)
        updated = False
        result = check_winner(game_board)
        if "Player" in result:
            print(result)
            break
        if not space_available(game_board):
            print("All options out, No one won !!!")
            break
        while not updated:
            player2 = input("Player 2 - Enter the row[1-3], column[1-3] : ")
            updated = update_matrix(2, player2, game_board)
        display_matrix(game_board)
        updated = False
        result = check_winner(game_board)
        if "Player" in result:
            print(result)
            break
    print("\nThanks for playing the game :-) !!! ")
