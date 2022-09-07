from collections import deque

A, B = map(int, input().split())
Q = deque([(A, 1)])

res = 0
while Q:
    n, cnt = Q.popleft()
    if n == B:
        res = 1
        break
    if n * 2 <= B:
        Q.append((n * 2, cnt + 1))
    if n * 10 + 1 <= B:
        Q.append((n * 10 + 1, cnt + 1))
if res:
    print(cnt)
else:
    print(-1)

# x × 2 연산과 y x 10 + 1 연산이 중복 발생하지 않아서
# 결과값이 겹칠 수 없으므로 방문체크를 해주지 않아도 됨