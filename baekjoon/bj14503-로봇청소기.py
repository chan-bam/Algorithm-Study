import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 세로크기 N # 가로크기 M
r, c, d = map(int, input().split()) # 시작 좌표 (r, c), 방향 d (북: 0, 동: 1, 남: 2, 서: 3)
space = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
# 북: 0, 동: 1, 남: 2, 서: 3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited[r][c] = 1
cnt = 1

while True:
    for _ in range(4):
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]
        if not space[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            r, c = nr, nc
            cnt += 1
            break
    else:
        nr, nc = r - dr[d], c - dc[d]
        if space[nr][nc]:
            print(cnt)
            exit(0)
        else:
            r, c = nr, nc




'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 세로크기 N # 가로크기 M
r, c, d = map(int, input().split()) # 시작 좌표 (r, c), 방향 d (북: 0, 동: 1, 남: 2, 서: 3)
space = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dr = [-1, 0, 1, 0] # 북, 동, 남, 서
dc = [0, 1, 0, -1]

# 시작위치 청소
visited[r][c] = 1
cnt = 1

# 청소
while True:
    flag = 0
    # 현재방향을 기준으로 왼쪽방향에
    for _ in range(4): # 4방향 회전
        # 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 "회전"한 다음 전진
        # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 "회전"만
        d = (d + 3) % 4     # 왼쪽 회전
        nr = r + dr[d]
        nc = c + dc[d]
        if not space[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            cnt += 1
            r, c = nr, nc # 전진
            flag = 1
            break
    if not flag:
        nr = r - dr[d]
        nc = c - dc[d]
        # 네 방향 모두 청소가 이미 되어있거나, 벽인 경우에는, 바라보는 방향을 유지한 채 한칸 후진
        if not space[nr][nc]:  # 뒤쪽 방향이 벽이 아닌 경우
            r, c = nr, nc # 후진
        # 네 방향 모두 청소가 이미 되어있거나, 벽이면서, 뒤쪽방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다
        else: # 뒤쪽방향이 벽인 경우
            print(cnt)  
            exit(0) # 작동 중지
            
# 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.
# => nr, nc 범위 체크 X
'''

