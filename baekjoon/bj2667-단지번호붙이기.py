import sys
input = sys.stdin.readline

N = int(input())
ARR = [list(map(int, input().rstrip())) for _ in range(N)]

def dfs(x, y):
    global cnt
    ARR[x][y] = 0
    cnt += 1
    for dr, dc in ([(1, 0), (-1, 0), (0, 1), (0, -1)]):
        nx, ny = x + dr, y + dc
        if 0 <= nx < N and 0 <= ny < N and ARR[nx][ny]:
            dfs(nx, ny)

num = 0 # == len(result)
result = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if ARR[i][j]:
            num += 1
            dfs(i, j)
            result.append(cnt)

result.sort() # 오름차순 정렬
print(num, *result, sep='\n')
