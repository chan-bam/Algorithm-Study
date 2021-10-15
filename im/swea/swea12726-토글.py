import sys
sys.stdin = open("12726in.txt")


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    # N X N 배열  # M초 (1초부터 M초까지 토글된다)

    BRD = [list(map(int, input().split())) for _ in range(N) ]

    for k in range(1, M + 1):  # 1초부터 M초까지
        for i in range(0, N):
            for j in range(0, N):
                if k == M or M % k == 0:  # M초가 됐거나 k가 M의 약수일때
                    if BRD[i][j] == 0:
                        BRD[i][j] = 1
                    else:
                        BRD[i][j] = 0
                elif (i+1 + j+1) % k == 0: # i+j가 k초로 나누어떨어지는 영역은 토글 (k이거나 k의 배수인 영역)
                    if BRD[i][j] == 0:
                        BRD[i][j] = 1
                    else:
                        BRD[i][j] = 0

    res = 0
    for b in BRD:
        res += b.count(1)
    print(f'#{tc} {res}')