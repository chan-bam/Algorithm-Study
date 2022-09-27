import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
# A를 B번 곱한 수를 C로 나눈 나머지

def dac(a, b): # 분할정복
    if b == 1:
        return a % C
    temp = dac(a,  b // 2) ** 2
    if b % 2: # 홀수
        return temp * a % C
    else: # 짝수
        return temp % C

print(dac(A, B))