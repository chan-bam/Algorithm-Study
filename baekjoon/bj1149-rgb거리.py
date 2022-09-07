import sys
input = sys.stdin.readline

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        RGB[i][j] = RGB[i][j] + min(RGB[i - 1][(j + 1) % 3], RGB[i - 1][(j + 2) % 3])

print(min(RGB[N - 1]))