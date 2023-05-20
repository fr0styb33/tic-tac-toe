from random import randrange

def display_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n---------")

def enter_move(board):
    while True:
        move = input("Adicione um movimento entre 1 e 9: ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9 and is_free(board, move):
                update_board(board, move, 'O')
                break
        print("Movimento inválido! Tente novamente.")

def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit():
                free_fields.append((i, j))
    return free_fields

def win_for(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = randrange(len(free_fields))
        row, col = free_fields[move]
        update_board(board, move + 1, 'X')

def is_free(board, move):
    for row in board:
        if str(move) in row:
            return True
    return False

def update_board(board, move, sign):
    for i in range(3):
        for j in range(3):
            if board[i][j] == str(move):
                board[i][j] = sign

def main():
    board = [['1', '2', '3'],
             ['4', 'X', '6'],
             ['7', '8', '9']]

    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if win_for(board, 'O'):
            print("Você venceu!!")
            break
        if len(make_list_of_free_fields(board)) == 0:
            print("Empatou!!")
            break
        draw_move(board)
        display_board(board)
        if win_for(board, 'X'):
            print("O computador venceu!")
            break

if __name__ == "__main__":
    main()
