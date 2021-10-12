import sys
sys.stdin = open("4408in.txt")

# 삼성시의 버스노선처럼...?

# 카운트배열
# 1과 맞은편의 2는 사실상 같은라인.... 동선이 겹치면 2가 됨..!
#############################
# 1 3 5 7 9 .... 397 399 #
# 2 4 6 8 10 ... 398 400 #
# 1+1 // 2 == 2 // 2
# 동선이 가장 많이 겹치는 시간이 "모든 학생들이 이동할 수 있는" 최소 시간이 됨

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 돌아가야 할 학생들
    # N 줄에 걸쳐 방의 목록이....
    # 방의 범위는 1 ~ 400 : 반으로 나누면 200
    room = [0 for _ in range(201)]
    stLst = []

    for n in range(N):
        start, target = map(int, input().split())
        stLst.append([start, target])

    # print(stLst)
    for st in stLst:
        # for i in range(201):
        #     if st[0] <= i <= st[1]:
        #         room[i] += 1
        for i in range(st[0], st[1]+1): # 시간초과난다....
            room[i] += 1
    print(f'#{tc} {max(room)}')



