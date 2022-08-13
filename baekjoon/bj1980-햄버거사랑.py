import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

if n > m:
    n, m = m, n

cnt = 0
coke = 0
remain_time = t

while remain_time:
    if remain_time < 0:
        coke += 1
        remain_time = t - coke
        cnt = 0
    elif not remain_time % n:
        cnt += remain_time // n
        remain_time = 0
    else:
        remain_time -= m
        cnt += 1

print(cnt, coke)



