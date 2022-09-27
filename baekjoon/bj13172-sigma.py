import sys
input = sys.stdin.readline
# from math import gcd

# a*b^(-1) =  a*b^(X-2)%X이므로  a*b^(X-2)%X를 시간 안에 해결해야 하는 문제

P = 1_000_000_007
M = int(input())

def DaC(n, p):
    if p == 1:
        return n % P
    temp = DaC(n, p // 2) ** 2 % P
    if p % 2: # 홀수이면
        return temp * n % P
    else: # 짝수이면
        return temp % P

result = 0
for _ in range(M):
    N, S = map(int, input().split()) # N면체 # 주사위에 적힌 숫자의 합

    # 기약분수 만들기 # 안해도 결과에 영향이 없음
    # g = gcd(N, S)
    # N, S = N // g, S // g

    # 주사위를 굴렸을 때 나오게 되는 숫자의 기댓값: S // N == a * b **(-1) ==  a * b **(1000000007-2) % 1000000007
    # result += (S * N ** (P - 2)) % P

    # N ** (P - 2)를 시간안에 구하기
    result += S * DaC(N, P - 2) % P
result %= P # !!!!!
print(result)