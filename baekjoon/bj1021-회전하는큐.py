from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
POS = list(map(int, input().split()))

cnt = 0
dq = deque([i + 1 for i in range(N)])
for p in POS:
    while dq[0] != p:
        idx = dq.index(p)
        if idx <= len(dq) // 2:
            dq.rotate(-1)
        else:
            dq.rotate(1)
        cnt += 1
    dq.popleft()
print(cnt)

'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
POS = list(map(int, input().split()))
cnt = 0

dq = deque([i + 1 for i in range(N)])
for p in POS:
    while True:
        if dq[0] == p:
            dq.popleft()
            break
        else:
            idx = dq.index(p) # 뽑아내려는 수의 위치
            if idx <= len(dq) // 2: # 앞에서 가까운 경우
                dq.rotate(-1) # 왼쪽으로 회전
                cnt += 1
            else: # 뒤에서 가까운 경우
                dq.rotate(1)
                cnt += 1 # 오른쪽으로 회전
print(cnt)
'''