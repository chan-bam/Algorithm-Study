import sys
input = sys.stdin.readline

def cut(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                cut(x, y, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return # !!!
    result[color] += 1 # 파란색 칸 1 하얀색 칸 0

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = [0] * 2
cut(0, 0, N)
print(*result, sep='\n', end='')