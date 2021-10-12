import sys
sys.stdin = open("1859.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split())) # 비용

    benefit = 0 # 이득

    maxV = cost[N-1] # 가장 마지막값으로 비교

    for i in range(N-2, -1, -1): # 뒤에서부터 비교
        if cost[i] >= maxV: # 가장 높은값이면
            maxV = cost[i] #높은값으로 max값 바꾼다
        benefit += (maxV - cost[i]) # 가장 높은값에서 현재 가격을 빼준다
    print(f'#{tc} {benefit}')