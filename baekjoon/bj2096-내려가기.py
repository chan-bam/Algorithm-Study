import sys
input = sys.stdin.readline

N = int(input())

# sliding window
dp_max, dp_min = [0] * 3, [0] * 3
tmp_max, tmp_min = [0] * 3, [0] * 3

for _ in range(N):
    x, y, z = map(int, input().split())
    for i in range(3):
        if not i:
            tmp_max[i] = x + max(dp_max[i:i + 2])
            tmp_min[i] = x + min(dp_min[i:i + 2])
        elif i == 1:
            tmp_max[i] = y + max(dp_max[i - 1:i + 2])
            tmp_min[i] = y + min(dp_min[i - 1:i + 2])
        else:
            tmp_max[i] = z + max(dp_max[i - 1:i + 1])
            tmp_min[i] = z + min(dp_min[i - 1:i + 1])
    dp_max = tmp_max[:]
    dp_min = tmp_min[:]

print(max(dp_max), min(dp_min))

'''
# 메모리초과
import sys
input = sys.stdin.readline

N = int(input())

ARR = [list(map(int, input().split())) for _ in range(N)]
dp_max = [[0] * 3 for _ in range(N)]
dp_min = [[0] * 3 for _ in range(N)]


for i in range(N):
    for j in range(3):
        if not i:
            dp_max[i][j] = ARR[i][j]
            dp_min[i][j] = ARR[i][j]
        else:
            if not j:
                dp_max[i][j] = ARR[i][j] + max(dp_max[i - 1][j:j + 2])
                dp_min[i][j] = ARR[i][j] + min(dp_min[i - 1][j:j + 2])
            elif j == 1:
                dp_max[i][j] = ARR[i][j] + max(dp_max[i - 1][j - 1:j + 2])
                dp_min[i][j] = ARR[i][j] + min(dp_min[i - 1][j - 1:j + 2])
            else:
                dp_max[i][j] = ARR[i][j] + max(dp_max[i - 1][j - 1:j + 1])
                dp_min[i][j] = ARR[i][j] + min(dp_min[i - 1][j - 1:j + 1])

print(max(dp_max[N - 1]), min(dp_min[N - 1]))
'''