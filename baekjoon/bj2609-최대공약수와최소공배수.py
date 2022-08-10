n, m = map(int, input().split())
# from math import gcd, lcm

# 최대공약수  # 다른 코드 참조함
def gcd(x, y):
    while y:  # y가 0이 될때까지
        x, y = y, x % y # x에 y 대입, y에 x를 y로 나눈 나머지 대입
    return x

# 최소공배수
def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(n, m))
print(lcm(n, m))