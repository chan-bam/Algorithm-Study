import sys
sys.stdin = open("4408in.txt")


# 삼성시의 버스노선처럼...?
# 자료형을 정의할 수도 있다.....? 이부분은 바로 적용시키기는 좀 어려운듯... map으로 받아서 변환해서 입력해야할듯..?
def div(num):
    return (int(num)+1)//2

# 카운트배열
# 1과 맞은편의 2는 사실상 같은라인.... 동선이 겹치면 2가 됨..!
#############################
# 1 3 5 7 9 .... 397 399 #
# 2 4 6 8 10 ... 398 400 #
# 1+1 // 2 == 2 // 2
# 동선이 가장 많이 겹치는 시간이 "모든 학생들이 이동할 수 있는" 최소 시간이 됨
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 돌아가야 할 학생들
    # N 줄에 걸쳐 방의 목록이....
    # 방의 범위는 1 ~ 400 : 반으로 나누면 200
    room = [0 for _ in range(201)]

    # 이렇게 인풋 받을 수도 있다
    students = [list(map(div, input().split())) for _ in range(N)]

    # print(students)
    for i in range(len(students)):
        # 학생의 이동 방향을 오름차순으로 정렬하라 # 테스트케이스와 이동순서는 다르게 들어올 수 있음
        if students[i][0] > students[i][1]: # 교환! # 지금의 테스트케이스의 경우에는 안해도 tc에는 이상 없지만..
            students[i][0], students[i][1] = students[i][1], students[i][0]
        for j in range(students[i][0], students[i][1]+1):
            room[j] += 1
    print(f'#{tc} {max(room)}')
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 돌아가야 할 학생들
    # N 줄에 걸쳐 방의 목록이....
    # 방의 범위는 1 ~ 400 : 반으로 나누면 200
    # 카운트배열
    room = [0 for _ in range(201)]
    stLst = []
    for n in range(N):
        start, target = map(int, input().split())
        stLst.append([(start+1)//2, (target+1)//2])

    # print(stLst)
    # 2차원배열의 인덱스 활용
    for i in range(len(stLst)): # 오름차순정렬
        if stLst[i][0] > stLst[i][1]:
            stLst[i][0], stLst[i][1] = stLst[i][1], stLst[i][0]

        # 정렬한 후 인덱스 기준으로 카운트배열에 1을 누적한다
        for j in range(stLst[i][0], stLst[i][1] + 1):
            room[j] += 1

    print(f'#{tc} {max(room)}')



