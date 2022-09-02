import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def bfs():

    while Q:
        node = Q.popleft()
        if node == goal:
            return
        D = node * 2 % 10_000
        if node: # !!!
            S = node - 1
        else:
            S = 9999
        L = node % 1000 * 10 + node // 1000
        R = node % 10 * 1000 + node // 10

        for x, y in [(D, 'D'), (S, 'S'), (L, 'L'), (R, 'R')]:
            if not visited[x]:
                Q.append(x)
                visited[x] = 1
                result[x] = result[node] + y


for _ in range(T):
    start, goal = map(int, input().split())
    visited = [0] * 10_000  # 0 ~ 9999 # visited를 문자열을 저장할 배열로 사용하는 경우 0으로 시작할 때 0번째 문자열에 불필요한 D가 저장되는 문제가 있음
    result = [''] * 10_000
    Q = deque([start])
    visited[start] = 1 # 시작값을 visited 처리하지 않는 경우 처음 시작이 0인 경우 0번째 문자열에 불필요한 D가 저장되는 문제가 있음
    bfs()
    print(result[goal])


'''
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def bfs():

    while Q:
        node = Q.popleft()
        if node == goal:
            return
        node_str = '0' * (4 - len(str(node))) + str(node) # 4자리
        D = node * 2 % 10_000
        if node: # !!!
            S = node - 1
        else:
            S = 9999
        L = int(node_str[1:len(node_str)] + node_str[0])
        R = int(node_str[len(node_str) - 1] + node_str[:-1])
        # print(L, R)
        DSLR = {'D': D, 'S': S, 'L': L, 'R': R}

        for key, value in DSLR.items():
            if not visited[value]:
                Q.append(value)
                visited[value] = visited[node] + key


for _ in range(T):
    start, goal = map(int, input().split())
    visited = [''] * 10_001  # 0 ~ 10000
    Q = deque([start])
    bfs()
    if start:
        print(visited[goal])
    else:
        print(visited[goal][1:])

'''


# 반례
# 1
# 0 1000
# 정답  SDDLDSLDRDDD
# 오답 DSDDLDSLDRDDD으로 맨 앞에 D가 추가되어서 나온다
# 0 * 0 = 0이므로 필요하지 않은 연산이기 때문에 방문 처리를 하지 않도록..?


'''
13
5 0
0 7
0 1000
9 0
47 63
26 60
60 50
32 38
98 366
5310 6
7519 2006
7579 4005
2720 8031

정답
RD
SDRDRDRDDSDR
SDDLDSLDRDDD
SDSRSD
RSDLS
RSSRR
RSL
RSLSSSD
SRDLSD
DRSSR
SDDRS
SRDDSDR
DDRSRDDS

'''
