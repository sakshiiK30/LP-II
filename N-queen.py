def solve_n_queens_first_solution(n):
    # Initialize state arrays
    column = [False] * n
    diag1 = [False] * (2 * n - 1)  # row + col
    diag2 = [False] * (2 * n - 1)  # row - col + n - 1
    board = [-1] * n  # board[i] = column index of queen in row i
    step = 1  # Step counter
    found = [False]  # Mutable flag to indicate solution is found

    def print_board_state(board, action, row=None, col=None):
        nonlocal step
        print(f"\nStep {step}: {action}")
        if row is not None and col is not None:
            print(f"    Row: {row}, Column: {col}")
        for i in range(n):
            line = ""
            for j in range(n):
                if board[i] == j:
                    line += " Q "
                else:
                    line += " . "
            print(line)
        step += 1

    def backtrack(row):
        if found[0]:
            return  # Stop recursion after first solution is found

        if row == n:
            print_board_state(board, "✔ Found a valid solution")
            found[0] = True
            return

        for col in range(n):
            if not column[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                # Place queen
                board[row] = col
                column[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                print_board_state(board, "Placing queen", row, col)

                backtrack(row + 1)

                if found[0]:
                    return  # Stop further backtracking

                # Remove queen (backtrack)
                column[col] = diag1[row + col] = diag2[row - col + n - 1] = False
                print_board_state(board, "Removing queen (backtracking)", row, col)

    backtrack(0)

# --- Main Program ---
try:
    n = int(input("Enter the number of queens (n ≥ 4 is recommended): "))
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        solve_n_queens_first_solution(n)
except ValueError:
    print("Invalid input. Please enter an integer.")
OUTPUT:
Enter the number of queens (n ≥ 4 is recommended): 4

Step 1: Placing queen
    Row: 0, Column: 0
 Q  .  .  .
 .  .  .  .
 .  .  .  .
 .  .  .  .

Step 2: Placing queen
    Row: 1, Column: 2
 Q  .  .  .
 .  .  Q  .
 .  .  .  .
 .  .  .  .

Step 3: Removing queen (backtracking)
    Row: 1, Column: 2
 Q  .  .  .
 .  .  Q  .
 .  .  .  .
 .  .  .  .

Step 4: Placing queen
    Row: 1, Column: 3
 Q  .  .  .
 .  .  .  Q
 .  .  .  .
 .  .  .  .

Step 5: Placing queen
    Row: 2, Column: 1
 Q  .  .  .
 .  .  .  Q
 .  Q  .  .
 .  .  .  .

Step 6: Removing queen (backtracking)
    Row: 2, Column: 1
 Q  .  .  .
 .  .  .  Q
 .  Q  .  .
 .  .  .  .

Step 7: Removing queen (backtracking)
    Row: 1, Column: 3
 Q  .  .  .
 .  .  .  Q
 .  Q  .  .
 .  .  .  .

Step 8: Removing queen (backtracking)
    Row: 0, Column: 0
 Q  .  .  .
 .  .  .  Q
 .  Q  .  .
 .  .  .  .

Step 9: Placing queen
    Row: 0, Column: 1
 .  Q  .  .
 .  .  .  Q
 .  Q  .  .
 .  .  .  .

Step 10: Placing queen
    Row: 1, Column: 3
 .  Q  .  .
 .  .  .  Q
 .  Q  .  .
 .  .  .  .

Step 11: Placing queen
    Row: 2, Column: 0
 .  Q  .  .
 .  .  .  Q
 Q  .  .  .
 .  .  .  .

Step 12: Placing queen
    Row: 3, Column: 2
 .  Q  .  .
 .  .  .  Q
 Q  .  .  .
 .  .  Q  .

Step 13: ✔ Found a valid solution
 .  Q  .  .
 .  .  .  Q
 Q  .  .  .
 .  .  Q  .
