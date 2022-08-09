import sys
sys.stdin = open("4875in.txt")

def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N and (maze[x][y] == 0 or maze[x][y] == 3)

def dfs(x,y):
    #목표점 도착 or 결과가 나왔다면 리턴
    global ans
    if maze[x][y] == 3 or ans:
        ans = 1
        return
    visited.append((x, y))

    for i in range(4): # 방향
        new_x = x + dx[i]
        new_y = y + dy[i]
        if is_safe(new_x, new_y) and (new_x, new_y) not in visited:
            dfs(new_x, new_y)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # NxN 가로세로 길이
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발점 찾기
    # x, y = 0, 0 # x행, y열
    visited = []
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2: # 출발점 2
                dfs(i, j)
                # x, y = i, j
    # visited = []
    # ans = 0
    # dfs(x,y)
    print(f'#{tc} {ans}')