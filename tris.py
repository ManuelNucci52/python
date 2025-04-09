def create_players():
    p1 = input("Giocatore 1 (X): ").strip() or "X"
    p2 = input("Giocatore 2 (O): ").strip() or "O"

    return p1, p2


def can_move(position):
    return not board[position].strip()


def make_move(position):
    board[position] = "X" if current_player == player1 else "O"


def choose_move():
    while True:
        try:
            position = int(input(f"{current_player}, fai la tua mossa (1-9): ").strip()) - 1

            if can_move(position):
                return make_move(position)

            print("Spazio già occupato!")
        except (ValueError, IndexError):
            print("Mossa non valida!")


def show_board():
    row_separator = "-" * 11
    col_separator = " | "

    print()
    print(f" {col_separator.join(board[0:3])} ")
    print(row_separator)
    print(f" {col_separator.join(board[3:6])} ")
    print(row_separator)
    print(f" {col_separator.join(board[6:9])} ")
    print()


def somebody_won():
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    return any(board[a] == board[b] == board[c] != " " for a, b, c in win_conditions)


def current_status():
    if somebody_won():
        return "V"
    elif " " not in board:
        return "X"
    else:
        return "N"


def next_player():
    return player2 if current_player == player1 else player1


print("Benvenuti su Tris!\n")

player1, player2 = create_players()

while True:
    current_player = player1
    board = [" "] * 9

    print()

    while True:
        choose_move()
        show_board()

        match current_status():
            case "N":
                current_player = next_player()
            case "X":
                print("Pareggio!")
                break
            case "V":
                print(f"Complimenti {current_player}, hai vinto!")
                break


    if input("\nVolete giocare ancora (S/N)? ").strip().upper() != "S":
        break