# swea 4698 특별한 소수

import sys
sys.stdin = open('swea4698in.txt')

######## 에라토스테네스의 체 ######## (VER4)
ARR = [True for _ in range(1000001)]  # True로 초기화

ARR[0] = ARR[1] = False   # 0, 1은 소수가 아니므로 False로 바꿔준다

for i in range(2, 1001):   # 범위의 제곱근까지...
    if ARR[i]:     # True이면
        for k in range(i + i, 1000001, i):
            ARR[k] = False  # 범위의 제곱근 이내에 있는 배수는 모두 False로 바꿔준다
#################################

T = int(input())

for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    # D: 테네스가 좋아하는 숫자 (포함되어있어야 하는 숫자) _ 1 ~ 9
    # A: A 이상 (소수 범위) _ 1 ~ 1000000
    # B: B 이하 (소수 범위) _ 1 ~ 1000000
    D = str(D)  # 문자열로 다시 변환

    cnt = 0
    for s in range(A, B+1):  # A 이상 B 이하 범위
        if ARR[s]:    # True이면 == 소수이면
            if D in str(s): # 소수이고 D 숫자가 포함되어있으면
                cnt += 1   # 개수를 늘려라

    print(f'#{tc} {cnt}')

'''
    ### 에라토스테네스의 체 ### (VER1)
    ###################################
    ARR = [True for _ in range(1000001)]    # True로 초기화

    ARR[0] = ARR[1] = False     # 0,1은 소수가 아니므로 False로 바꿔준다

    for i in range(1001): # 범위의 제곱근까지...
        if ARR[i]:
            for k in range(i+i, 1000001, i):
                ARR[k] = False  # 범위의 제곱근 이내에 있는 배수는 모두 False로 바꿔준다
    # print(ARR[:10])
    #####################################
'''

'''
    ### 에라토스테네스의 체 ### (VER2)
    ###################################
    ARR = [True for _ in range(B+1)]    # True로 초기화

    ARR[0] = ARR[1] = False     # 0,1은 소수가 아니므로 False로 바꿔준다

    for i in range(int(B**0.5)+1): # 범위의 제곱근까지...
        if ARR[i]:
            for k in range(i+i, B+1, i):
                ARR[k] = False  # 범위의 제곱근 이내에 있는 배수는 모두 False로 바꿔준다
    # print(ARR[:10])
    #####################################
'''

'''
    ### 에라토스테네스의 체 ### (VER3)
    ###################################
    ARR = [True for _ in range(B+1)]    # True로 초기화

    ARR[0] = ARR[1] = False     # 0,1은 소수가 아니므로 False로 바꿔준다

    for i in range(int(B**0.5)+1): # 범위의 제곱근까지...
        if ARR[i]:
            for k in range(i+i, B+1, i):
                ARR[k] = False  # 범위의 제곱근 이내에 있는 배수는 모두 False로 바꿔준다
    # print(ARR[:10])
    #####################################
'''