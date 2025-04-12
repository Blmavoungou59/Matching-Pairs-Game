import random
import time

def create_board():
    items = ['🍎', '🍌', '🍇', '🍓', '🍍', '🍉'] * 2
    random.shuffle(items)
    return [items[i:i+4] for i in range(0, len(items), 4)]

def display_board(board, revealed):
    for i in range(3):
        row = ""
        for j in range(4):
            if revealed[i][j]:
                row += f" {board[i][j]} "
            else:
                row += " * "
        print(row)
    print()

def get_coords(prompt):
    while True:
        try:
            x, y = map(int, input(prompt).split())
            if 0 <= x < 3 and 0 <= y < 4:
                return x, y
            else:
                print("Coordinates out of range. Try again.")
        except:
            print("Invalid input. Enter row and column separated by space (e.g., 1 2).")

def play_game():
    board = create_board()
    revealed = [[False]*4 for _ in range(3)]
    matches = 0

    print("🧠 Welcome to Matching Pairs Game!")

    while matches < 6:
        display_board(board, revealed)
        x1, y1 = get_coords("Select the first card (row col): ")
        if revealed[x1][y1]:
            print("Card already revealed. Choose another one.")
            continue
        revealed[x1][y1] = True
        display_board(board, revealed)

        x2, y2 = get_coords("Select the second card (row col): ")
        if revealed[x2][y2]:
            print("Card already revealed. Choose another one.")
            revealed[x1][y1] = False
            continue
        revealed[x2][y2] = True
        display_board(board, revealed)

        if board[x1][y1] == board[x2][y2]:
            print("🎉 It's a match!")
            matches += 1
        else:
            print("❌ Not a match. Try again!")
            time.sleep(2)
            revealed[x1][y1] = False
            revealed[x2][y2] = False

    print("🏆 Congratulations! You found all matches!")

if __name__ == "__main__":
    play_game()
