import sys

sys.stdin = open("1940.txt")

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sumV = 0 # 이동한 거리를 누적할 변수
    speed = 0 # 초기 속도
    for c in range(N):
        command = list(map(int, input().split()))

        if command[0] == 0:  # 기존 속도를 유지
            sumV += speed  # 거리(속도*1초)를 누적

        elif command[0] == 1:  # 가속시키기
            speed += command[1]  # 가속시킬 속도만큼 속도를 증가시킨다
            sumV += speed # 거리(속도*1초)를 누적

        elif command[0] == 2:  # 감속시키기
            if speed >= command[1]:  # 현재 속도가 감속할 속도보다 클때
                speed -= command[1]   # 현재 속도에서 감속할 속도를 뺀다
            else:  # 현재 속도가 감속할 속도보다 작을때
                speed = 0  # 속도는 0
            sumV += speed # 거리(속도*1초)를 누적

    print(f'#{tc} {sumV}')  # N초 동안 이동한 거리
'''

# 코드 수정 (sumV += speed가 중복되므로 if문 밖에서 수행해도 무방)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sumV = 0 # 이동한 거리를 누적할 변수
    speed = 0 # 초기 속도
    for c in range(N):
        command = list(map(int, input().split()))

        if command[0] == 1:  # 가속시키기
            speed += command[1]  # 가속시킬 속도만큼 속도를 증가시킨다

        elif command[0] == 2:  # 감속시키기
            if speed >= command[1]:  # 현재 속도가 감속할 속도보다 클때
                speed -= command[1]   # 현재 속도에서 감속할 속도를 뺀다
            else:  # 현재 속도가 감속할 속도보다 작을때
                speed = 0  # 속도는 0

        # command[0] == 0일때는 속도 유지하므로 그냥 처리
        sumV += speed # 거리(속도*1초)를 누적

    print(f'#{tc} {sumV}')  # N초 동안 이동한 거리