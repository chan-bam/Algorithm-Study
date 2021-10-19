import sys
sys.stdin = open("1954in.txt")

T = int(input())

dr = [0, 1, 0, -1] # 우 # 하 # 좌 # 상
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    # 초기값 지정
    nr = nc = dir = 0
    snail[0][0] = 1
    for i in range(2, N**2+1):
        # 범위체크 및 숫자 있는지 체크
        nr += dr[dir]
        nc += dc[dir]

        if nr < 0 or N <= nr or nc < 0 or N <= nc or snail[nr][nc] != 0:
            nr -= dr[dir]
            nc -= dc[dir]
            dir = (dir + 1)%4 # 방향전환
            nr += dr[dir]
            nc += dc[dir]
        snail[nr][nc] = i

        # 범위에 지장 없으면...

    print(f'#{tc}')
    for s in snail:
        print(*s)
