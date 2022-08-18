N = int(input())

people = list(map(int, input().split()))

people.sort()
time = 0
for i in range(N + 1):
    for j in range(0, i):
        time += people[j]
print(time)
