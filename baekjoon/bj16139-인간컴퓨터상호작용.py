import sys
input = sys.stdin.readline

S = input().rstrip()
N = int(input())
cnt = [[0] * 26]

# print(ord('z'), ord('a'))
for i in range(len(S)):
    w = S[i]
    cnt[i][ord(w) - 97] += 1
    cnt.append(cnt[i][:])

for _ in range(N):
    w, s, e = input().split()
    tmp = ord(w) - 97
    if s == '0':
        print(cnt[int(e)][tmp])
    else:
        print(cnt[int(e)][tmp] - cnt[int(s) - 1][tmp])