
import sys
sys.stdin = open("10158in.txt")
input = sys.stdin.readline
# X: (시작좌표:5 + 시간:4) // 6 = 1 -- 홀수 : (축전체길이6-나머지3=3)   ==>> 3
# Y: (시작좌표:3 + 시간:4) // 4 = 1 -- 홀수: (축전체길이4-나머지3=1)  ==>> 1
# ===>> (3, 1)

def move(x, o): # x는 시간에 따라 일직선으로 쭉 이동한 위치 # o는 격자길이
    d, m = divmod(x, o) # x를 o로 나눈 몫,나머지를 반환하는 함수
    if d % 2:  # 몫이 홀수이면
        return o - m  # 격자크기 - 나머지 가 그래프에 있는 값
    # 몫이 짝수이면
    return m  # 나머지가 그래프에 있는 값


TC = int(input())
for tc in range(TC):
    w, h = map(int, input().split())   # 가로, 세로

    p, q = map(int, input().split())   # 초기위치의 좌표값 (x, y)

    t = int(input()) # 개미가 움직일 시간 t

    # 시간에 따라 일직선상으로 쭉 보냈다 생각하고 해당 좌표와 가로세로 격자판 길이를 기준으로 좌표를 구한다
    print(move(p+t, w), move(q+t, h))
            # 시간마다 1칸씩 이동하므로
            # 원래좌표 + 시간, 해당하는 축의 격자크기
            # ...를 기준으로 계산