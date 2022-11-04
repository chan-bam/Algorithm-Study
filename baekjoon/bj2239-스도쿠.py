import sys
input = sys.stdin.readline

def solve(depth):
    if depth == len(zero):
        for s in sudoku:
            print(*s, sep='')
        exit()
    x, y = zero[depth]
    for n in range(1, 10):
        if horizon(n, x) and vertical(n, y) and square(n, x, y):
            sudoku[x][y] = n
            solve(depth + 1)
            sudoku[x][y] = 0

def horizon(num, r):
    # for k in range(9):
    #     if sudoku[r][k] == num:
    #         return False
    if num in sudoku[r]:
        return False
    return True

def vertical(num, c):
    for k in range(9):
        if sudoku[k][c] == num:
            return False
    return True

def square(num, r, c):
    nr, nc = r // 3 * 3, c // 3 * 3
    # for k in range(3):
    #     for m in range(3):
    #         if sudoku[nr + k][nc + m] == num:
    #             return False
    if num in sudoku[nr][nc:nc + 3] or num in sudoku[nr + 1][nc:nc + 3] or num in sudoku[nr + 2][nc:nc + 3]:
        return False
    return True

zero = []
sudoku = [list(map(int, input().rstrip())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            zero.append((i, j))
solve(0)