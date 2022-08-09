# 5174

import sys
sys.stdin = open("5174.txt")

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    print(E, N)
