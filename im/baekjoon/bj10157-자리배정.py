import sys
sys.stdin = open("10157in.txt")

# 달팽이숫자네... # 델타
# 열, 행을 그대로 사용한다면 2차원 배열의 모습은 상하가 반대로 된 모습이다 # 진행순서도 상,하는 반대가 된다
# NxN아니라 입력에 따라 유동적 # 진행방향 상하 반대로 # 행,열(R,C) 순아니라 열,행(C,R)순으로 출력해야함
# 2차원배열을 상,우,하,좌달팽이방향으로 채우면서 target번호 나오면 좌표를 반환 # (0,0)부터 시작하는 게 아니라 조정해야하기는 할듯.. +1 +1?
# 모든 좌석이 배정되어 해당 대기번호의 관객에게 좌석을 배정할 수 없다...  대기번호가 NxN 개수 넘어가면 배정못하지않나?

def seat():
    ARR = [[0] * C for _ in range(R)]  # C가 열 # R이 행
    i = 1
    nr = nc = dir = 0
    ARR[nr][nc] = 1  # 초기값
    while i < K:  # K까지만 반복
        nr += dr[dir]  # 진행 방향으로 전진
        nc += dc[dir]
        if nr < 0 or R <= nr or nc < 0 or C <= nc or ARR[nr][nc] != 0:  # 범위를 벗어났거나 숫자가 이미 있을 때는...
            # 좌표 초기화 및 방향전환
            nr -= dr[dir]
            nc -= dc[dir]
            dir = (dir + 1) % 4  # 4 넘어가지 않도록
        else:
            i += 1  # 입력했을 때만 i + 1
            ARR[nr][nc] = i

    return nc+1, nr+1 # C, R순 출력

dr = [1, 0, -1, 0]  # 하, 우, 상, 좌 순
dc = [0, 1, 0, -1 ]

for tc in range(int(input())):
    # 공연장의 크기
    C, R = map(int, input().split())
    K = int(input())
    if C*R < K: # 대기번호가 좌석
        print(0)
    else:
        print(*seat())

