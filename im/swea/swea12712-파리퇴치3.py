import sys
sys.stdin = open("12712in.txt")


def catch(x, y, arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        sumV = 0
        for j in range(M):
            if 0 <= nx < N and 0 <= ny < N:
                # print(arr[x][y])
                sumV += arr[x][y]

                nx = nx + dx[i]
                ny = ny + dy[i]
    return sumV

T = int(input())
for tc in range(1, T+1):
    # N X N 배열  /  M : 스프레이를 분사한 세기
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]



    maxV = 0
    for i in range(N): # 분사한 세기
        for j in range(N):
            flySum = catch(i, j, fly)
            # print(flySum)
            if maxV < flySum:
                maxV = flySum
    print(maxV)