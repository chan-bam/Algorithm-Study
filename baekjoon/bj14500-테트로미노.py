import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 세로크기 N, 가로크기 M
paper = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
for i in range(N):
    for j in range(M):
        # 2 x 2 -  ㅁ모양
        if i < N - 1 and j < M - 1:
            maxV = max(maxV, paper[i][j] + paper[i + 1][j] + paper[i][j + 1] + paper[i + 1][j + 1])
        # 1 x 4 - ㅡ 모양
        if i < N and j < M - 3:
            maxV = max(maxV, paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i][j + 3])
        # 4 x 1 - ㅣ 모양
        if i < N - 3 and j < M:
            maxV = max(maxV, paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 3][j])
        # 2 x 3 Z모양  &  ㅜ ㅗ & ㄱ ㄴ * 2
        if i < N - 1 and j < M - 2:
            a = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + max(paper[i + 1][j + 2], paper[i][j + 2])
            b = paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j] + max(paper[i][j + 2], paper[i + 1][j + 2])
            c = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + max(paper[i + 1][j], paper[i + 1][j + 2])
            d = paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2] + max(paper[i][j], paper[i][j + 2])
            maxV = max(maxV, a, b, c, d)
        # 3 x 2 Z모양 & ㅏ ㅓ & ㄱ ㄴ * 2
        if i < N - 2 and j < M - 1:
            a = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + max(paper[i + 2][j + 1], paper[i + 2][j])
            b = paper[i + 1][j] + paper[i][j + 1] + paper[i + 1][j + 1] + max(paper[i + 2][j], paper[i + 2][j + 1])
            c = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + max(paper[i][j + 1], paper[i + 2][j + 1])
            d = paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1] + max(paper[i][j], paper[i + 2][j])
            maxV = max(maxV, a, b, c, d)
print(maxV)

# pypy3 592ms
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 세로크기 N, 가로크기 M
paper = [list(map(int, input().split())) for _ in range(N)]

maxV = 0

# 2 x 2 -  ㅁ모양
for i in range(N - 1):
    for j in range(M - 1):
        maxV = max(maxV, paper[i][j] + paper[i + 1][j] + paper[i][j + 1] + paper[i + 1][j + 1])

# 1 x 4 - ㅡ 모양
for i in range(N):
    for j in range(M - 3):
        maxV = max(maxV, paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i][j + 3])

# 4 x 1 - ㅣ 모양
for i in range(N - 3):
    for j in range(M):
        maxV = max(maxV, paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 3][j])

# 2 x 3 Z모양  &  ㅜ ㅗ & ㄱ ㄴ * 2
for i in range(N - 1):
    for j in range(M - 2):
        a = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + max(paper[i + 1][j + 2], paper[i][j + 2])
        b = paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j] + max(paper[i][j + 2], paper[i + 1][j + 2])
        c = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + max(paper[i + 1][j], paper[i + 1][j + 2])
        d = paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2] + max(paper[i][j], paper[i][j + 2])
        maxV = max(maxV, a, b, c, d)


# 3 x 2 Z모양 & ㅏ ㅓ & ㄱ ㄴ
for i in range(N - 2):
    for j in range(M - 1):
        a = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + max(paper[i + 2][j + 1], paper[i + 2][j])
        b = paper[i + 1][j] + paper[i][j + 1] + paper[i + 1][j + 1] + max(paper[i + 2][j], paper[i + 2][j + 1])
        c = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + max(paper[i][j + 1], paper[i + 2][j + 1])
        d = paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1] + max(paper[i][j], paper[i + 2][j])
        maxV = max(maxV, a, b, c, d)

print(maxV)

# pypy3 268ms
'''