import sys
sys.stdin = open("4831in.txt")

T = int(input())

for tc in range(1, T+1):
    # 한번 충전으로 최대한 이동할 수 있는 정류장 수 : K - CAN_GO
    # 충전기가 설치된 M개의 정류장 번호 : M - LAST_STOP
    # 0번에서 충전해 종점인 N번 정류장까지 이동 : N - CHARGER
    CAN_GO, LAST_STOP, CHARGER = map(int, input().split())

    #충전기가 설치된 정류장 리스트
    charge_stop = list(map(int, input().split()))

    curPos = 0
    cnt = 0

    while curPos + CAN_GO < LAST_STOP: # 현재위치+최대한 이동할 수 있는 정류장이 종점이전이면
        for step in range(CAN_GO, 0, -1): # 최대한 이동할 수 있는 정류장 수까지 갈 수 있으므로 최대한 이동할 수 있는 정류장수부터~(1번째까지) 가는 것을 고려했을때...
            if (curPos + step) in charge_stop: # 충전기가 설치된 정류장 리스트 안에 있으면
                curPos += step # 현재위치에서 충전기가 있는 정류장 위치만큼 더해서 이동한다
                cnt += 1  # cnt에 충전횟수를 추가한다
                break  # for문을 빠져나온다
        else: # 최대한 이동할 수 있는 정류장 범위 내에 충전기가 설치된 정류장을 만날 수 없는 경우
            cnt = 0  # cnt를 0으로 만든다
            break

    print(f'#{tc} {cnt}')  # cnt를 출력한다














'''

T = int(input())

for tc in range(1, T+1):
    # 한번 충전으로 최대한 이동할 수 있는 정류장 수 : K - CAN_GO
    # 충전기가 설치된 M개의 정류장 번호 : M - LAST_STOP
    # 0번에서 충전해 종점인 N번 정류장까지 이동 : N - CHARGER 
    
    CAN_GO, LAST_STOP, CHARGER = map(int, input().split())
    charge_num = list(map(int, input().split()))

    # 필요한 변수들 초기화 (현재위치, 카운트)
    curPos = 0
    cnt = 0

    while curPos + CAN_GO < LAST_STOP:
        for step in range(CAN_GO, 0, -1):
            if (curPos + step) in charge_num:
                curPos += step
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
'''