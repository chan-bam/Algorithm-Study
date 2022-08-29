import sys
input = sys.stdin.readline

def cut(r, c, n):
    color = paper[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != color:
                acc = n // 3
                for k in range(0, acc * 2 + 1, acc):
                    for m in range(0, acc * 2 + 1, acc):
                        cut(r + k, c + m, acc)
                return
    result[color + 1] += 1

N = int(input())
paper = [list(map(int, input().split()))for _ in range(N)]
result = [0] * 3
cut(0, 0, N)
print(*result, sep='\n', end='')