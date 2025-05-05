def print_board(elements):
    for i in range(0, 9, 3):
        print(elements[i:i+3])
    print()

def solvable(start):
    inv = 0
    for i in range(9):
        if start[i] <= 1:
            continue
        for j in range(i + 1, 9):
            if start[j] == 0:
                continue
            if start[i] > start[j]:
                inv += 1
    return inv % 2 == 0

def heuristic(state, goal):
    h = 0
    for i in range(9):
        if state[i] == 0:
            continue
        j = goal.index(state[i])
        h += abs(j // 3 - i // 3) + abs(j % 3 - i % 3)
    return h

def move(state, pos1, pos2):
    temp = state[:]
    temp[pos1], temp[pos2] = temp[pos2], temp[pos1]
    return temp

def get_neighbors(state):
    empty = state.index(0)
    row, col = divmod(empty, 3)
    moves = []

    if col > 0:
        moves.append(move(state, empty, empty - 1))
    if col < 2:
        moves.append(move(state, empty, empty + 1))
    if row > 0:
        moves.append(move(state, empty, empty - 3))
    if row < 2:
        moves.append(move(state, empty, empty + 3))
    return moves

def solve_puzzle(start, goal):
    visited = set()
    steps = 0
    print(f"Step {steps}:")
    print_board(start)

    while start != goal:
        visited.add(tuple(start))
        neighbors = get_neighbors(start)
        unvisited = [n for n in neighbors if tuple(n) not in visited]

        if not unvisited:
            print("No solution found (got stuck).")
            return

        start = min(unvisited, key=lambda x: heuristic(x, goal))
        steps += 1
        print(f"Step {steps}:")
        print_board(start)

    print(f" Puzzle solved in {steps} moves.")

# -------- INPUT --------
print("Enter the start state of the puzzle (0 represents the blank tile):")
start = []
for i in range(1, 4):
    row = input(f"Enter row {i} (3 numbers separated by spaces): ").split()
    start.extend([int(num) for num in row])

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

if solvable(start):
    solve_puzzle(start, goal)
else:
    print(" This puzzle is unsolvable.")

OUTPUT:
Enter the start state of the puzzle (0 represents the blank tile):
Enter row 1 (3 numbers separated by spaces): 1 2 3
Enter row 2 (3 numbers separated by spaces): 0 4 6
Enter row 3 (3 numbers separated by spaces): 7 5 8
Step 0:
[1, 2, 3]
[0, 4, 6]
[7, 5, 8]

Step 1:
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Step 2:
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Step 3:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

 Puzzle solved in 3 moves.
