# pypy3만 통과

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
sum_arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not j:
            sum_arr[i][j] = arr[i][0]
        else:
            sum_arr[i][j] = sum_arr[i][j - 1] + arr[i][j]

for _ in range(M):
    total = 0
    x1, y1, x2, y2 = map(int, input().split())
    if y1 == 1:
        for i in range(x1 - 1, x2):
            total += sum_arr[i][y2 - 1]
    else:
        for i in range(x1 - 1, x2):
            total += sum_arr[i][y2 - 1] - sum_arr[i][y1 - 2]

    print(total)

'''
# pypy3만 통과
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
sum_arr = [[0] * N for _ in range(N)]
sum_arr[0][0] = arr[0][0]

for i in range(N):
    for j in range(N):
        if not i and not j:
            continue
        elif j:
            sum_arr[i][j] = sum_arr[i][j - 1] + arr[i][j]
        else:
            sum_arr[i][j] = sum_arr[i - 1][N - 1] + arr[i][j]

for _ in range(M):
    total = 0
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        total = arr[x2 - 1][y2 - 1]
    elif y1 == 1:
        for i in range(x1 - 1, x2):
            if i:
                total += sum_arr[i][y2 - 1] - sum_arr[i - 1][N - 1]
            else:
                total += sum_arr[i][y2 - 1]
    elif y1 >= 2:
        for i in range(x1 - 1, x2):
            total += sum_arr[i][y2 - 1] - sum_arr[i][y1 - 2]
    print(total)
'''

'''
# 시간초과
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0
    for x in range(x1 - 1, x2):
        for y in range(y1 - 1, y2):
            total += arr[x][y]
    print(total)
'''

