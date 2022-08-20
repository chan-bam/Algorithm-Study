N = int(input())

f = 1
for i in range(1, N + 1):
    f *= i

cnt = 0
while not f % 10:
    f = f // 10
    cnt += 1

print(cnt)