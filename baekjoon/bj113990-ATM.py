N = int(input())

people = list(map(int, input().split()))

people.sort()

time = 0
time_acc = 0

for i in range(N):
    time += people[i]
    time_acc += time

    # for j in range(i):
    #     time += people[j]
print(time_acc)
