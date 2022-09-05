from math import factorial, comb

n, m = map(int, input().split())
if n < m:
    n, m = m, n
print(comb(n, m))
# print(factorial(n) // (factorial(n-m) * factorial(m)))