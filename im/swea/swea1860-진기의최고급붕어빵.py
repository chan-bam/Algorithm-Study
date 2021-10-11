# import sys
# sys.stdin = open("1860in.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))    # 사람들이 방문하는 초를 정렬
    max_sec = people[-1]    #
    bread = 0

    res = 'Possible'
    for i in range(max_sec+1):  # 1초부터 마지막 사람이 방문한 초까지...
        if i != 0 and i % M == 0:   # 0초 아니고 초가 M초로 나누어떨어지면 M초의 배수초이면
            bread += K      # 빵의 개수를 K개 늘린다
        if i in people:     # people (사람들이 방문하는 초에 해당하면)
            if bread > 0:   # 빵의 개수가 1개 이상히면
                bread -= 1  # 빵의 개수를 1 줄인다
            else:        # 빵의 개수가 0개 이하이면 # 팔 수 없음
                res = 'Impossible'   # impossible로 바꿈
                break       # 반복문 종료

    print(f'#{tc} {res}')

'''

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))

    max_sec = people[-1]
    bread = [0] * (max_sec + 1)

    for i in range(M, max_sec+1, M):
        for j in range(i, max_sec+1):
            bread[j] += K

    # print(bread)

    res = 'Possible'
    for k in people:
        if bread[k] > 0:
            for m in range(k, max_sec+1):
                bread[m] -= 1
        else:
            res = 'Impossible'
    # print(bread)

    print(f'#{tc} {res}')
'''