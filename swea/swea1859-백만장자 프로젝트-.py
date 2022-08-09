# 보충 교수님 코드

# 백만장자 프로젝트
# 뒤에서부터 최댓값을 비교하여 최댓값이 갱신될 때 까지 차이를 이윤으로 누적하는 방식
# 1개씩만 살 수 있으니까 앞에 더 큰 값이 나오면 무조건 그 날에 파는것이 이득이라서..!!(?맞게 이해한건지는 모르겠음)

import sys
sys.stdin = open("1859.txt")

# 인덱스 연습
# 오른쪽으로 오는 것도 이해 못할 정도로 복잡한 코드 아니니.....!!
# 설명을 들었을 때 아~~ 그렇게 구현하면 되겠구나 하고 구현할 수 있을 정도로 연습이 되어있어야 한다

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    s = 0   # 총 이익
    maxV = cost[N-1]     # 마지막 날 가격으로 초기화

    for i in range(N-2, -1, -1):
        if maxV > cost[i]:  # 이익을 남길 수 있는 경우
            s += maxV - cost[i]
        maxV = max(maxV, cost[i])
    print(f'#{tc} {s}')



'''
# im시험의 주 목적 : 인덱스 연습
# 시간초과 - im수준에서는 시간초과는 잘 안나긴 함... # 모든구간에서의 최대값 찾기
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    s = 0 # 총 이익

    for i in range(N-1): # 물건 구입으 고려하는 날(마지막날은 제외)
        maxV = cost[i+1] #팔수있는 구간의 첫번째날 가격
        for j in range(i+2, N): # 팔 수 있는 모든 날 중에
            if maxV < cost[j]:
                maxV = cost[j]
        if cost[i] < maxV:
            s += maxV - cost[i]  # i날 물건을 사서 이익을 남길 수 있으면...
    print(f'#{tc} {s}')
'''