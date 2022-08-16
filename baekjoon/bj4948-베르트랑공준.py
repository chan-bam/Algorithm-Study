import sys
input = sys.stdin.readline

eratos = [1 for _ in range(123456 * 2 + 1)]
eratos[1] = 0
for i in range(2, 123456 * 2 + 1):
    for j in range(i * 2, 123456 * 2 + 1, i):
        eratos[j] = 0

while True:
    number = int(input().rstrip())
    if number == 0:
        break
    else:
        print(eratos[number + 1:number * 2 + 1].count(1))
