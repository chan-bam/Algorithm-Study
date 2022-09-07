import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

# Divide and Conquer로 푸는 문제
def DaC(a, b):
    if b == 1:
        return a % C
    elif not b % 2: # 짝수
        return (DaC(a, b // 2) ** 2) % C
    else: # 홀수
        return (DaC(a, b // 2) ** 2 * a) % C

print(DaC(A, B))
# print(A ** B % C) # O(n) - 시간초과
