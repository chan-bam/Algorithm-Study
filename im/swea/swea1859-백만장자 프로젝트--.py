# 앞에서부터 짜기
# 시간초과

import sys
sys.stdin = open("1859.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    benefit = 0

    for i in range(N-1): # 기준가격
        maxV = cost[i+1] # 판매할 수 있는 날의 가격으로 초기화
        for j in range(i+1, N): # 판매를 고려할 수 있는 날의 범위
            if maxV <= cost[j]: # i인덱스 이후의 값 중에서 최대값 찾기
                maxV = cost[j]  # 최대값 갱신
        if cost[i] < maxV: # 최대값보다 작으면
            benefit += (maxV - cost[i]) # 이득을 볼 수 있는 차이 값을 누적
    print(f'#{tc} {benefit}')