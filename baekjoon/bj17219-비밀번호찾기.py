import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

password = {}

for _ in range(N):
    a, b = input().rstrip().split()
    password[a] = b

for _ in range(M):
    print(password[input().rstrip()])