# 백만장자 프로젝트
# 뒤에서부터 최댓값을 비교하여 최댓값이 갱신될 때 까지 차이를 이윤으로 누적하는 방식
# 1개씩만 살 수 있으니까 앞에 더 큰 값이 나오면 무조건 그 날에 파는것이 이득이라서..!!(?맞게 이해한건지는 모르겠음)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    max_cost = cost[-1] #최대금액 변수를 마지막날의 금액으로 초기값 설정
    benefit = 0 # 이윤을 저장할 변수 초기화

    for i in range(N-2, -1, -1): #마지막에서 2번째번지부터 0까지 1씩 감소하면서 비교(최대값이 마지막날 값으로 설정되어있으므로 마지막날은 비교할 필요가 없음)
        if cost[i] < max_cost: # 최대값보다 비교하는 날짜의 값이 작으면 #사야되는 날
            benefit += (max_cost - cost[i]) # 이윤(최대값-비교하는 날짜의 값)을 누적
        else:
            if cost[i] > max_cost: # 최대값보다 비교하는 날짜의 값이 크면 #안사는 날
                max_cost = cost[i] # 최대값을 비교하는 날짜의 값으로 변경한다 # 이후 다음값은 이 값과 비교

    print('#{} {}'.format(tc, benefit))




















'''
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = lst[::-1] # 리스트를 뒤집는다 # 마지막날부터 판단
    benefit = 0  # 이득을 저장할 변수 초기화
    i = 0
    while i < N: # 마지막날(0번인덱스)를 기준으로 비교 시작
        for j in range(i+1, N): # 마지막날의 다음날부터 순차적으로 비교
            cnt = 0
            if lst[i] > lst[j]: # 마지막날의 값보다 그 다음날의 값이 작으면 : 이득O
                benefit += (lst[i]-lst[j]) #마지막 날의 값에서 다음날의 값을 뺀 값을 이득으로 저장
                cnt += 1
            else: # 마지막 날의 값에 비해 비교하는 값이 크거나 같으면.... 이득X
                i += cnt
                break

    print('#{} {}'.format(tc, benefit))
'''