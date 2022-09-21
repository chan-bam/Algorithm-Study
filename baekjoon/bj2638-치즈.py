import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    global cnt
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not cheese[nx][ny] and not visited[nx][ny]: # 공기
                visited[nx][ny] = 1
                dfs(nx, ny)
            elif cheese[nx][ny] and not visited[nx][ny]: # 한 변에 접촉한 치즈
                visited[nx][ny] = 1
            elif cheese[nx][ny] and visited[nx][ny]: # 두 변에 접촉한 치즈
                cheese[nx][ny] = 0 # 녹음
                cnt += 1 # 녹인 개수 누적

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    dfs(0, 0)
    if not cnt:
        break
    time += 1

print(time)
