import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Q = [i + 1 for i in range(N)]
idx = 0
result = []
while Q:
    idx = (idx + K - 1) % len(Q) # 요소가 1개씩 줄어듬 => index가 K - 1씩 증가 & index가 배열 길이보다 커질 수 없음
    result.append(Q.pop(idx))
print('<', end = '')
print(*result, sep=', ', end = '')
print('>')
