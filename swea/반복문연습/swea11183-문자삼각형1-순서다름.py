import sys
sys.stdin = open("11183in.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    sumV = 0
    print(f'#{tc}')
    for i in range(1, N+1):  # 높이 N까지
        print(' ' * (N-i+1), end='')
        for j in range(1, i+1):
            sumV += 1 # 1씩 누적
            print(chr(sumV+64), end = ' ') # 누적한 값을 출력
        print()


'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ARR = [[] for i in range(N)]

    sumV = 0
    print(f'#{tc}')
    for i in range(0, N):  # 높이 N까지
        for j in range(0, i+1):
            sumV += 1 # 1씩 누적
            ARR[i].append(chr(sumV+64)) # 누적한 값을 출력
    print(ARR)
    '''