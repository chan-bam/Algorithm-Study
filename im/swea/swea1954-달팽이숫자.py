import sys
sys.stdin = open("1954in.txt")

T = int(input())


# 우 하 좌 상 우
dr = [0, 1, 0, -1] # 행  # 우 하 좌 상
dc = [1, 0, -1, 0] # 열  # 방향 주의 !!!

for tc in range(1, T+1):
    N = int(input())

    snail = [[0]*N for _ in range(N)]   # 배열 초기화
    nr = nc = 0     # nr, nc 초기화

    dir = 0     # 델타 방향 초기값 0번인덱스

    for i in range(1, N*N+1): # 1부터 N**2 까지
        snail[nr][nc] = i    # i값 저장
        nr += dr[dir]   # 저장된 방향으로 이동
        nc += dc[dir]   # 저장된 방향으로 이동

        if nr < 0 or N <= nr or nc < 0 or N <= nc or snail[nr][nc] != 0 : # 범위 벗어나거나 값이 0이 아니면(값이 0이 아닌 조건 때문에 안쪽으로 도는 모양으로 출력되게 된다)
            nr -= dr[dir]
            nc -= dc[dir]   # 초기화해주고

            dir = (dir + 1) % 4 # 방향 바꾼다
            nr += dr[dir]   # 방향 바꾼 값으로 인덱스 전환
            nc += dc[dir]   # 방향 바꾼 값으로 인덱스 전환

    print(f'#{tc}')
    for res in snail:
        print(*res)     # 리스트 한줄 공백으로 묶어서 출력해줌