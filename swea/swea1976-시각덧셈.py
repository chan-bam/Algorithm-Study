# 시각 덧셈

import sys
sys.stdin = open("1976.txt")

T = int(input())

for tc in range(1, T+1):
    # 첫번째 시간, 분 / 두번째 시간, 분
    T1, M1, T2, M2 = map(int, input().split())
    resT = T1 + T2 # 시간을 더한다
    resM = M1 + M2 # 분을 더한다
    if M1 + M2 >= 60: # 더한 분이 60분을 넘으면
        resT += 1 # 시간에 1을 더하고
        resM -= 60 # 분에서 60분을 뺀다
    if resT > 12: # 12시간제로 표기하므로 12시가 넘는 경우
        resT -= 12 # 시간에서 12를 뺀다
    print('#{} {} {}'.format(tc, resT, resM))