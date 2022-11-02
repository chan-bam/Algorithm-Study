import sys
input = sys.stdin.readline

def solve(idx):
    if idx == len(points):
        for s in sudoku:
            print(*s)
        exit(0)
    x, y = points[idx]
    nx, ny = x // 3 * 3, y // 3 * 3
    for k in range(1, 10):
        flag = 0
        for m in range(9):
            if sudoku[m][y] == k:
                flag = 1
                break
        if not flag and k not in sudoku[x] and k not in sudoku[nx][ny:ny + 3] and k not in sudoku[nx + 1][ny:ny + 3] and k not in sudoku[nx + 2][ny:ny + 3]:
            sudoku[x][y] = k
            solve(idx + 1)
            sudoku[x][y] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]
points = []
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            points.append((i, j))
solve(0)

'''
testcase
0 0 0 0 4 3 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 5 0 0 0 0
0 8 0 7 0 0 0 2 0
0 6 0 0 0 0 0 0 3
0 0 0 0 0 0 0 4 0
0 0 5 8 0 0 6 0 0
4 0 0 1 0 0 0 0 0
3 0 0 0 0 0 5 0 0
result
6 7 1 9 4 3 2 5 8
5 4 2 6 8 7 1 3 9
8 3 9 2 5 1 4 6 7
1 8 3 7 6 4 9 2 5
9 6 4 5 2 8 7 1 3
2 5 7 3 1 9 8 4 6
7 1 5 8 3 2 6 9 4
4 9 6 1 7 5 3 8 2
3 2 8 4 9 6 5 7 1

testcase
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
result
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
'''
