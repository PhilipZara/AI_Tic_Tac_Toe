import random

BOARD_WIDTH = 3
BOARD_HEIGHT = 3


def new_board():
    board = [[None for _ in range(BOARD_HEIGHT)] for _ in range(BOARD_WIDTH)]
    return board


def render(board):
    rows = []
    for i in range(BOARD_WIDTH):
        row = []
        for j in range(BOARD_HEIGHT):
            row.append(board[i][j])
        rows.append(row)
    print("    0  1  2")
    print("  -----------")
    for x in range(len(rows)):
        output = "{} |".format(x)
        for y in range(len(rows[x])):
            if rows[x][y] is None:
                output += "   "
            else:
                output += " " + rows[x][y] + " "
        print(output + "|")
    print("  -----------")


def get_move():
    x = int(input("What is your move's X co-ordinate?: "))
    y = int(input("What is your move's Y co-ordinate?: "))
    move_coords = (x, y)
    return move_coords


def make_move(board, co_ordinates, player):
    next_board = board
    try:
        if next_board[co_ordinates[0]][co_ordinates[1]] is None:
            next_board[co_ordinates[0]][co_ordinates[1]] = player
        else:
            print("Invalid move! Square already occupied. Try again!")
            get_move()
    except IndexError:
        print("Oops you are out of range. Try again!")
        get_move()
    return next_board


def get_lines_co_ords():
    rows = []
    cols = []
    for x in range(BOARD_WIDTH):
        row = []
        for y in range(BOARD_HEIGHT):
            row.append((x, y))
        rows.append(row)

    for i in range(BOARD_WIDTH):
        col = []
        for j in range(BOARD_HEIGHT):
            col.append((j, i))
        cols.append(col)

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    return rows + cols + diagonals


def get_winner(board):
    line_co_ords = get_lines_co_ords()
    for line in line_co_ords:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]

    return None


def full_board(board):
    for col in board:
        for sqr in col:
            if sqr is None:
                return False
    return True


def random_ai(board):
    legal_moves = []
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[x][y] is not None:
                continue
            else:
                legal_moves.append((x, y))

    random_move = random.randint(0, len(legal_moves) - 1)
    for i in range(len(legal_moves)):
        return legal_moves[random_move]


def its_play_time():
    player1 = "X"
    player2 = "O"
    player_turn = 0
    board = new_board()
    while True:
        if player_turn % 2 == 0:
            make_move(board, get_move(), player1)
        else:
            make_move(board, random_ai(board), player2)
        render(board)
        winner = get_winner(board)
        if winner is not None:
            render(board)
            print("Congrats! The winner is {}".format(winner))
            break
        if full_board(board):
            render(board)
            print("It's a Draw!")
            break
        player_turn += 1


if __name__ == '__main__':
    its_play_time()
