import sys
sys.stdin = open("1979in.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 가로, 세로 길이 N, 단어의 길이 K

    ARR = [list(map(int, input().split())) for _ in range(N)]

    # print(ARR)
    res = []

    for i in range(N):
        sumV = 0
        for j in range(N): # 행우선
            if ARR[i][j] == 0: # NxN이라서 세로도 같이 탐색해도 무방하다...
                res.append(sumV)
                sumV = 0
            else:
                sumV += 1
        res.append(sumV)

    for y in range(N):
        sumV2 = 0
        for x in range(N):
            if ARR[x][y] == 0: # 열우선
                res.append(sumV2)
                sumV2 = 0
            else:
                sumV2 += 1
        res.append(sumV2)


    print(f'#{tc} {res.count(K)}')