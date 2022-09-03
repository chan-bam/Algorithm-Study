import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 세로크기 N, 가로크기 M
board = [list(map(int, input().split())) for _ in range(N)]
max_val = max(map(max, board)) # 모든 좌표 중 최댓값
visited = [[0] * M for _ in range(N)]
maxV = 0

def dfs(x, y, sumV, cnt):
    global maxV
    if sumV + max_val * (4 - cnt) <= maxV: # 지금 있는 값에 board에서 제일 큰 값을 (4 - cnt)번 더해도 maxV보다 작으면 return
        return
    if cnt == 4:
        maxV = max(maxV, sumV)
        return
    # 상하좌우 방향으로 블록 이어 붙여 나가기
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if cnt == 2: # ㅏ ㅓ ㅗ ㅜ 만들기
                # 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색 재개
                visited[nx][ny] = 1
                dfs(x, y, sumV + board[nx][ny], cnt + 1) # 기존좌표 x, y
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, sumV + board[nx][ny], cnt + 1)
            visited[nx][ny] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, board[i][j], 1)
        visited[i][j] = 0

print(maxV)