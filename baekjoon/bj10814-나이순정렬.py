N = int(input())
member = [[] for _ in range(201)]
for _ in range(N):
    age, name = input().split()
    member[int(age)].append(name)
    
for m in range(len(member)):
    if member[m]:
        for mem in member[m]:
            print(f'{str(m)} {mem}')