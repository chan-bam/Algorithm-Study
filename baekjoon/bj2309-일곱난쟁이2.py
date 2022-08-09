N = []
for i in range(9):
    temp = int(input())
    N.append(temp)

N = sorted(N)

total_sum = sum(N)

goal = total_sum - 100

for i in range(len(N)):
    for j in range(len(N)):
        if N[i] + N[j] == goal:
            r1 = N[i]
            r2 = N[j]
            break
N.remove(r1)
N.remove(r2)

for k in N:
    print(k)