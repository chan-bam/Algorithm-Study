n = int(input())

D = [0, 1, 2]

for i in range(n + 1):
    D.append(D[-1] + D[-2])

print(D[n] % 10007)