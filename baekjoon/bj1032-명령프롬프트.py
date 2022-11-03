import sys
input = sys.stdin.readline
N = int(input())
files = [input() for _ in range(N)]
result = list(files[0])
L = len(result)

for i in range(1, N):
    for j in range(L):
        if result[j] != files[i][j]:
            result[j] = '?'
print(*result, sep='')

'''
# 참조용 코드
n = int(input())
a = list(input())

for _ in range(n - 1):
    b = list(input())
    for i in range(len(a)):
        if a[i] != b[i]:
            a[i] = '?'
print(''.join(a))
'''