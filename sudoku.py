
puzzle = [
    [3,9,-1, -1,5,-1, -1,-1,-1],
    [-1,-1,-1, 2,-1,-1, -1,-1,5],
    [-1,-1,-1, 7,1,9, -1,8,-1],
    [-1,5,-1, -1,6,8, -1,-1,-1],
    [2,-1,6, -1,-1,3, -1,-1,-1],
    [-1,-1,-1, -1,-1,-1, -1,-1,4],
    [5,-1,-1, -1,-1-1, -1,-1,-1],
    [6,7,-1, 1,-1,5, -1,4,-1],
    [1,-1,9, -1,-1,-1, 2,-1,-1],
]
def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None

def is_valid(puzzle, guess, row, col):
    
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i, col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # 3x3 box
    row_start = (row // 3) * 3
    col_start = (row // 3) * 3

    for i in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            return False

    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # where I can go?

    row, col = find_next_empty(puzzle)
    
    if row is None:
        return True

    # Step 2: if there's a place to put a guess...

    for guess in range(1, 10):
        # Step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3.1: if this is valid, then place the guess on the puzzle
            puzzle[row][col] = guess
            # nw recurse using this puzzle
            # Step 4: recursivly call our function
            if solve_sudoku(puzzle):
                return True
        # Step 3.2 in not valid guess...
        puzzle[row][col] = -1
    
    # Step 5: sudoku unsolvable
    return False

if __name__ == '__main__':
    example_board = puzzle
    
    print(solve_sudoku(example_board))
    print(example_board)