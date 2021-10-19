import sys
sys.stdin = open("1859in.txt")

T = int(input())
# 이방식도 런타임 에러 발생함

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    benefit = 0
    cnt = 0
    money = 0

    is_sell = [False] * N
    # i날 기준으로 이후에 더 비싼 날이 있는지 체크 # 어차피 이후에 최대값으로 팔게 됨 # 이후에 더 비싼날이 없으면 그 날이 팔아야 하는 날
    for i in range(N-1):
        for j in range(i+1, N):
            if cost[i] < cost[j]:
                is_sell[i] = True
                break

    for i in range(N): # 이방식은 마지막날까지 봐야한다.... 팔아야하는 날이 있기 때문
        if is_sell[i]: # 사야되는 날
            cnt += 1 # 물건을 산 개수를 카운팅
            money += cost[i] # 물건을 산 비용을 누적
        else: # 팔아야되는 날 # 더 비싼 금액이 뒤에 안나오는 날
            benefit += (cost[i]*cnt) - money # 최대값과 개수를 곱해 판매비용을 구하고 그동한 구매한 누적 비용을 빼서 이득을 누적한다
            cnt = 0 # 팔았으므로 물건 개수 초기화
            money = 0 # 팔았으므로 누적된 구매비용 초기화

    print(f'#{tc} {benefit}')
