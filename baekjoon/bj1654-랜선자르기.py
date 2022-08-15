import sys
input = sys.stdin.readline

K, N = map(int, input().split()) # 랜선의 개수 K # 필요한 랜선의 개수 N
cables = [int(input()) for _ in range(K)]

start, end = 1, max(cables)

# binary search
while start <= end:
    middle = (start + end) // 2
    cnt = 0
    for c in cables:
        if c >= middle:
           cnt += c // middle   # 몫을 더하면 케이블 개수
    if cnt >= N:
        start = middle + 1
    else:
        end = middle - 1
print(end)