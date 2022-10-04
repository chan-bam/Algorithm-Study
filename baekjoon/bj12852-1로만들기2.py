import sys
from collections import deque
input = sys.stdin.readline

X = int(input())
trace = [0] * (X + 1)
Q = deque([1]) # 1에서 시작해서 X까지 가는 최단경로 구하기
while Q:
    n = Q.popleft()
    if n * 3 == X or n * 2 == X or n + 1 == X:
        trace[X] = n
        break
    for i in (n * 3, n * 2, n + 1):
        if i < X and not trace[i]:
            trace[i] = n
            Q.append(i)

result = [X]
# 역추적
while result[-1] != 1: # 1을 만날때까지
    before = result[-1]
    result.append(trace[before])

print(len(result) - 1)
print(*result)




'''
import sys
from collections import deque
input = sys.stdin.readline

X = int(input())
trace = [0] * (X + 1)

Q = deque([1])
while Q:
    n = Q.popleft()
    if n * 3 == X or n * 2 == X or n + 1 == X:
        trace[X] = n
        break
    if n + 1 < X and not trace[n + 1]:
        Q.append(n + 1)
        trace[n + 1] = n
    if n * 3 < X and not trace[n * 3]:
        Q.append(n * 3)
        trace[n * 3] = n
    if n * 2 < X and not trace[n * 2]:
        Q.append(n * 2)
        trace[n * 2] = n

result = [X]
while result[-1] != 1:
    before = result[-1]
    result.append(trace[before])

print(len(result) - 1)
print(*result)
'''

'''

# 시간초과
import copy, sys
input = sys.stdin.readline

def dfs(x, cnt, arr):
    global result, trace
    arr2 = copy.deepcopy(arr)
    arr2.append(x)
    if x == 1:
        if cnt < result:
            result = cnt
            arr.append(1)
            trace = arr
        return
    if not x % 3:
        dfs(x // 3, cnt + 1, arr2)
    if not x % 2:
        dfs(x // 2, cnt + 1, arr2)
    dfs(x - 1, cnt + 1, arr2)

X = int(input())
result = sys.maxsize
trace = []
dfs(X, 0, [])
print(result)
print(*trace)
'''