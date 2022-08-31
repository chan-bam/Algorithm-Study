import sys
input = sys.stdin.readline

N = int(input())
M = int(input()) # S의 길이
S = input().rstrip()
res = 0
cnt = 0
i = 0
while i < M - 2:
    if S[i:i + 3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == N:
            cnt -= 1
            res += 1
    else:
        cnt = 0
        i += 1
print(res)