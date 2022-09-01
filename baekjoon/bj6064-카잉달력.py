import sys
input = sys.stdin.readline

# result % M = x % M
# result % N = y % N

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    result = x
    ny = y % N # result % N == y % N
    L = lcm(M, N) # 최소공배수
    # while result <= M * N and result % N != ny: # 곱한 값을 기준으로 해도 정답
    while result <= L and result % N != ny:
        result += M
    # if result > M * N:
    if result > L:
        print(-1)
    else:
        print(result)


'''
# 시간초과
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    i, j = 1, 1
    year = 1
    while True:
        if i < M:
            i += 1
        else:
            i = 1
        if j < N:
            j += 1
        else:
            j = 1
        year += 1
        if i == x and j == y:
            break
        if i == M and j == N:
            year = -1
            break
    print(year)
'''