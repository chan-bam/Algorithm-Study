# LED전등이 있다.
# on/ off 기능이 있다. on은 1 off는 0 으로 표시
# 시작은 모두 꺼진상태인 0 으로 본다.
#
# 예시
#  1 2 3 4 5 6
#  0 0 0 0 0 0
#
# 예를 들어 N = 6이면 6만큼의 길이를 가진 리스트가 그 다음줄에 입력으로 주어지는데
# 2번 버튼을 누르면 2뿐만 아니라 2의 배수인 4와 6까지 불이 켜진다.
#
# 1. 2번버튼을 클릭할 겨우 2의 배수가 다 불이 켜진다.
# 1 2 3 4 5 6
# 0 1 0 1 0 1
#
# 2. 이 상태에서 3번 버튼을 클릭할 경우 3의 배수에 불이 다 켜진다.
# 1 2 3 4 5 6
# 0 1 1 1 0 0
#
# 이때 6의 경우 2의 배수에 의해 불이 켜졌지만 다시 3의배수에 의해 꺼진것을 확인할 수 있다.
#
# 이런식으로 다 꺼진 시작상태에서 주어진 테스트케이스 리스트처럼 만들어야하는데
# 최소 몇회 조작해서 만들 수 있을지 반환하기
#
# 출력예시
#1 3
#2 2
#3 1
#4 1
#5 8

import sys
sys.stdin = open("im.txt")

T = int(input())

for tc in range(1, T+1):
    lenB = int(input())
    RES = [0] * lenB

    BULB = list(map(int, input().split()))

    cnt = 0

    for i in range(lenB):
        if BULB[i] != RES[i]:
            for j in range(i, lenB, i+1):
                if RES[j] == 0:
                    RES[j] = 1
                else:
                    RES[j] = 0
            cnt += 1
            if RES == BULB:
                break

    print(f'#{tc} {cnt}')
