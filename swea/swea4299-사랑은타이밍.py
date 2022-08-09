# 태혁이의 사랑은 타이밍
import sys
sys.stdin = open("4299.txt")

T = int(input())

for tc in range(1, T+1):
    # 소개팅 약속 시간은 2011.11.11 오전 11:11
    # 태혁이가 깨달음을 얻은 시간은 D일 H시 M분
    # D (11 ≤ D ≤ 14), H (0 ≤ H ≤ 23), M (0 ≤ M ≤ 59)
    D, H, M = map(int, input().split())
    resD = D - 12 # 소요된 일자 구하기
    # D가 11일으로 resD가 음수가 되는 경우에도 시간, 분과 더해져 맞는 결과값이 나온다...
    resH = H + (23 - 11) # 소요된 시간 구하기
    resM = M + (60 - 11) # 소요된 분 구하기
    res = resD*24*60 + resH*60 + resM # 분으로 환산하여 결과값으로 반영
    if res < 0: # 분으로 환산된 결과값이 0보다 작은 경우 # 11일 11시 11분 이전에 차인 것이므로
        res = -1 # -1을 결과값으로 반영
    print('#{} {}'.format(tc, res)) # 결과값 출력

'''
for tc in range(1, T + 1):
    # 소개팅 약속 시간은 2011.11.11 오전 11:11
    # 태혁이가 깨달음을 얻은 시간은 D일 H시 M분
    # D (11 ≤ D ≤ 14), H (0 ≤ H ≤ 23), M (0 ≤ M ≤ 59)
    D, H, M = map(int, input().split())
    if D == 11:  # 11일 당일인 경우
        if H < 11 and M < 11:  # 11시 11분 전에 차인 경우
            res = -1  # -1을 return
        else:  # 11시 11분 이후인 경우
            res = (H - 11) * 60 + (M - 11)
    else:  # 11일 이후인 경우
        resD = D - 12  # 소요된 일자 구하기
        resH = H + (23 - 11)  # 소요된 시간 구하기
        resM = M + (60 - 11)  # 소요된 분 구하기
        res = resD * 24 * 60 + resH * 60 + resM  # 분으로 환산
    print('#{} {}'.format(tc, res))  # 환산된 값 출력
'''