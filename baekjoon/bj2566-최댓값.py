import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]

result = -1
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if result < arr[i][j]:
            result = arr[i][j]
            x, y = i + 1, j + 1
        if result == 99:
            print(result)
            print(x, y)
            exit(0)
print(result)
print(x, y)