def tic_tac_toe_winner(board):
    lines = []

    # Filas y columnas
    for i in range(3):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])

    # Diagonales
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != "" and line.count(line[0]) == 3:
            return line[0]

    return "Draw"

# Ejemplo
game = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]

print(tic_tac_toe_winner(game))  # X
