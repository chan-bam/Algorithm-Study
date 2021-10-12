import sys
sys.stdin = open("12712in.txt")

# 인덱스에러 try except 시도했으나... 파이썬은 음수인덱스가 있어서 구현 불가능 # 범위 지정해야함

def catch(x, y):
    # 범위 체크 필수 !!!
    sumV = sumV2 = ARR[x][y] # 분사위치에서 초기화
    for a in range(1, M):
        if 0 <= x - a:
            sumV += ARR[x - a][y]
        if x + a < N:
            sumV += ARR[x + a][y]
        if 0 <= y - a:
            sumV += ARR[x][y - a]
        if y + a < N:
            sumV += ARR[x][y + a]

    for b in range(1, M):
        if 0 <= x - b and 0 <= y - b:
            sumV2 += ARR[x - b][y - b]
        if x + b < N and y + b < N:
            sumV2 += ARR[x + b][y + b]
        if 0 <= x - b and y + b < N:
            sumV2 += ARR[x - b][y + b]
        if x + b < N and 0 <= y - b:
            sumV2 += ARR[x + b][y - b]

    return sumV, sumV2


def catchD(m, k):
    sumW = sumH = ARR[m][k]
    for c in range(1, M):
        for d in range(4):
            # 가로세로
            nr = m + dr[d]*c
            nc = k + dc[d]*c

            # 대각선
            nr2 = m + dr[d+4]*c
            nc2 = k + dc[d+4]*c

            # 가로세로 범위 맞을 때만!!!
            if 0 <= nr < N and 0 <= nc < N:
                sumW += ARR[nr][nc]

            # 대각선 범위 맞을때만!!!
            if 0 <= nr2 < N and 0 <= nc2 < N:
                sumH += ARR[nr2][nc2]

    return sumW, sumH

# 8방향
dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, -1, 1]


T = int(input())
for tc in range(1, T+1):
    # N X N 배열  /  M : 스프레이를 분사한 세기
    N, M = map(int, input().split())

    ARR = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        for j in range(N):
            flySum = max(catchD(i, j))

            if maxV < flySum:
                maxV = flySum

    print(f'#{tc} {maxV}')