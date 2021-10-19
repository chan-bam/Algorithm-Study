import sys
sys.stdin = open("1859in.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))
    benefit = 0
    for i in range(N-1):
        maxV = cost[i+1] # 팔수 있는 첫번째 날로 초기화
        for j in range(i+2, N): # 초기화 다음날부터 비교
            if maxV < cost[j]: # 최대값이면
                maxV = cost[j] # 갱신
        if maxV > cost[i]: # 최대값보다 현재가격이 작으면
            benefit += maxV - cost[i] # 판 가격을 누적하고 현재 비용을 뺀다
    print(f'#{tc} {benefit}')