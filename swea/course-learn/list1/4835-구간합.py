import sys
sys.stdin = open("4835in.txt")

T = int(input())

for tc in range(1, T+1):
    # 정수의 개수 N과 구간의 개수 M
    N, M = map(int, input().split())
    LST = list(map(int, input().split()))

    maxV = 0
    minV = 10000*M

    for i in range(0, N-M+1):
        sumV = 0
        for j in range(i, i+M):
            sumV += LST[j]

        if maxV < sumV:
            maxV = sumV
        if minV > sumV:
            minV = sumV

    print(f'#{tc} {maxV - minV}')