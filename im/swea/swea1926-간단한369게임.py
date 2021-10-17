import sys
# sys.stdin = open("1926in.txt")


N = int(input())
result = []
for n in range(1, N+1):
    if '3' in str(n) or '6' in str(n) or '9' in str(n):
        cnt = str(n).count('3') + str(n).count('6') + str(n).count('9')
        result.append('-'*cnt)
    else:
        result.append(n)
print(*result)
