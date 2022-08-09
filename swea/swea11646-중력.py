import sys
sys.stdin = open("11646in.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    boxs = list(map(int, input().split()))

    maxCnt = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if boxs[i] > boxs[j]:
                cnt += 1
        if maxCnt < cnt:
            maxCnt = cnt
    print(f'#{tc} {maxCnt}')