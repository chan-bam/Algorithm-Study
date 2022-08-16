import sys

X = int(sys.stdin.readline())

a = 1
b = 1
d = [[0, 1], [1, -1], [1, 0], [-1, 1]]
x = 0

for i in range(1, X):
    a += d[x][0]
    b += d[x][1]
    if a <= 1 or b <= 1:
        x = (x + 1) % 4

print(a, '/', b, sep='')
