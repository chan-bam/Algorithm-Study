import sys
input = sys.stdin.readline

M, N = map(int, input().split())
words = {}
for _ in range(M):
    words[input().rstrip()] = 1
cnt = 0
for _ in range(N):
    cnt += words.get(input().rstrip(), 0)
print(cnt)
