import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y):
    global cnt
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            if cheeze[nx][ny]:
                cheeze[nx][ny] = 0
                cnt += 1
            else:
                dfs(nx, ny)

time = 0
while True:
    visited = [[0] * M for _ in range(N)] # 1
    cnt = 0 # !
    dfs(0, 0)
    if not cnt:
        break
    result = cnt
    time += 1

print(time)
print(result)