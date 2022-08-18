import sys
input = sys.stdin.readline

N, K = map(int, input().split())

score = list(map(int, input().split()))

score.sort(reverse=True)

print(score[K - 1])