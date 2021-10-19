# 앞에서부터 짜기
# 시간초과

import sys
sys.stdin = open("1859in.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    benefit = 0

    for i in range(N-1):
        maxV = cost[i+1] # 판매가 가능한 첫번째날로 초기화
        for j in range(i+1, N):
            if cost[j] > maxV: # i날 이후로 가장 비싼값을 찾는다
                maxV = cost[j]
        if cost[i] < maxV: # 찾은 최대값보다 i날 비용이 더 작은지
            benefit += (maxV - cost[i])
    print(f'#{tc} {benefit}')