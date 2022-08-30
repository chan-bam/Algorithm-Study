import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
move = {}
for _ in range(N):
    x, y = map(int, input().split())
    move[x] = y
for _ in range(M):
    u, v= map(int, input().split())
    move[u] = v

Q = deque([1])
visited = [0] * 101
while Q:
    x = Q.popleft()
    for i in range(1, 7):
        nx = x + i
        if nx <= 100 and not visited[nx]:
            if move.get(nx, 0):
                # visited[nx] = visited[x] + 1 # visited check 유무는 결과에는 영향 X
                nx = move[nx]
            if not visited[nx]: # 사다리, 뱀을 타고 이동한 값인 경우 visited 다시 check하여 queue에 추가
                visited[nx] = visited[x] + 1
                Q.append(nx)
print(visited[100])

'''
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
move = {}
for _ in range(N):
    x, y = map(int, input().split())
    move[x] = y
for _ in range(M):
    u, v= map(int, input().split())
    move[u] = v

Q = deque([1])
visited = [0] * 101

while Q:
    x = Q.popleft()
    if x == 100:
        break
    for i in range(1, 7):
        nx = x + i
        if nx <= 100 and visited[nx] < visited[x]:
            if move.get(nx, 0):
                visited[nx] = visited[x] + 1
                nx = move[nx]
                if not visited[nx]: # !!!!
                    visited[nx] = visited[x] + 1
                    Q.append(nx)
            else:
                visited[nx] = visited[x] + 1
                Q.append(nx)
print(visited[100])
'''