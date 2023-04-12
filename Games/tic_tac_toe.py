import tkinter as tk

# Создаем игровое поле
board = [["-" for i in range(3)] for j in range(3)]

# Создаем главное окно
root = tk.Tk()
root.title("Крестики-нолики")

# Функция для отображения текущего состояния игрового поля
def draw_board():
    for i in range(3):
        for j in range(3):
            # Отображаем крестик или нолик в соответствующей ячейке
            if board[i][j] == "X":
                tk.Label(root, text="X", font=("Arial", 40)).grid(row=i, column=j)
            elif board[i][j] == "O":
                tk.Label(root, text="O", font=("Arial", 40)).grid(row=i, column=j)
            # Отображаем пустую ячейку
            else:
                tk.Button(root, text=" ", font=("Arial", 40), command=lambda row=i, col=j: make_move(row, col)).grid(row=i, column=j)

# Функция для проверки выигрыша
def check_win(player):
    # Проверяем все возможные комбинации для выигрыша
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Функция для заполнения ячейки на игровом поле
def make_move(row, col):
    global current_player
    # Проверяем, что выбранная ячейка не занята
    if board[row][col] == "-":
        board[row][col] = current_player
        # Отображаем текущее состояние игрового поля
        draw_board()
        # Проверяем выигрыш
        if check_win(current_player):
            tk.messagebox.showinfo("Победа!", f"Победил игрок {current_player}")
            root.quit()
        # Сменяем игрока
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Запускаем игру
current_player = "X"
draw_board()
root.mainloop()