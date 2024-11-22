# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

# Loop through each row
for row in tic_tac_toe_board:
    # Loop through each element in the row
    for cell in row:
        print(cell, end=" ")  # Print each element with a space after it
    print()  # After each row, move to the next line
