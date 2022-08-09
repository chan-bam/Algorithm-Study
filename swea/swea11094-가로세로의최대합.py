import sys
sys.stdin = open("11094in.txt")

T = int(input())

for tc in range(1, T+1):
    # N x N 배열
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    # print(ARR)
    ARR2 = list(zip(*ARR))
    maxV = 0

    sumLst = []
    sumLst2 = []
    for i in range(N):
        sumLst.append(sum(ARR[i]))
        sumLst2.append(sum(ARR2[i]))
    # print(sumLst)
    # print(sumLst2)
    for i in range(N):
        sumV = 0
        for j in range(N):
            sumV = sumLst[i] + sumLst2[j] - ARR[i][j]
            # print(sumV)
            if sumV > maxV:
                maxV = sumV
    print(f'#{tc} {maxV}')
    max