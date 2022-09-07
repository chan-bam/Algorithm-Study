import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [[0] + list(map(int, input().split())) for _ in range(2)]
    for i in range(2, N + 1):
        arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
        arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])
        # for j in range(2):
        #     arr[j][i] += max(arr[j ^ 1][i - 1], arr[j ^ 1][i - 2])
    print(max(arr[0][N], arr[1][N]))
