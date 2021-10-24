import sys
sys.stdin = open("11176in.txt")
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    ARR = [[] for _ in range(N)]

    for i in range(N):
        if i % 2 == 0: # 짝수행이면
            for j in range(1, N+1):
                ARR[i].append(j + i*N)
        else: # 홀수행이면
            for k in range(N, 0, -1):
                ARR[i].append(k + i*j)
    print(ARR)

    for a in range(N): # 열
        for b in range(N): # 행
            print(chr((ARR[b][a])+64), end=' ')
        print()