import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # 라우터 내부에 존재하는 버퍼의 크기
router = deque()

# 한줄에 하나씩 라우터가 처리해야할 정보가 주어진다.
while True:
    num = int(input())
    if num == -1:
        break
    if num and len(router) < N:
        router.append(num)
    elif not num:
        router.popleft()

if router:
    print(*router)
else:
    print('empty')