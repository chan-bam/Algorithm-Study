import sys
sys.stdin = open("1979in.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 가로, 세로 길이 N, 단어의 길이 K

    # 0으로 가로 좌우 벽 추가해서 치기
    ARR = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    ARR = [[0]*(N+2)] + ARR + [[0]*(N+2)]  # 위아래 벽 추가하기

    # print(ARR)
    res = []

    for i in range(N+2):
        sumV = 0
        for j in range(N+2): # 행우선
            if ARR[i][j] == 0:
                res.append(sumV)
                sumV = 0
            else:
                sumV += 1
    # print(res)

    for y in range(N+2):
        sumV2 = 0
        for x in range(N+2):
            if ARR[x][y] == 0: # 열우선
                res.append(sumV2)
                sumV2 = 0
            else:
                sumV2 += 1

    print(f'#{tc} {res.count(K)}')