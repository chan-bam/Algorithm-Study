import sys
input = sys.stdin.readline
from math import lcm

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    y %= N
    result = x
    LCM = lcm(M, N)
    while result <= LCM and result % N != y:
        result += M
    if result > LCM:
        print(-1)
    else:
        print(result)