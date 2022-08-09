import sys
sys.stdin = open("1860in.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))    # 사람들이 방문하는 초를 정렬
    max_sec = people[-1]
    bread = 0

    for i in range(0, max_sec+1):  # 0초~마지막 사람이 방문한 초 ## 0초부터 사람이 올 수 있다고 함....
        if i != 0 and i % M == 0:   # 초가 M초로 나누어떨어지면 M초의 배수초이면
            bread += K      # 빵의 개수를 K개 늘린다
        if i in people:     # people (사람들이 방문하는 초에 해당하면)
            if bread > 0:   # 빵의 개수가 1개 이상히면
                bread -= 1  # 빵의 개수를 1 줄인다 # 방문해서 빵이 팔렸으므로
            else:        # 빵의 개수가 0개 이하이면 # 팔 수 없음
                res = 'Impossible'
                break       # 반복문 종료
    else:
        res = 'Possible' # 처음에 for문 조건 자체가 거짓일때 또는 break 없이 다 돈 후(마지막에 for문 조건이 거짓이 되므로?)

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