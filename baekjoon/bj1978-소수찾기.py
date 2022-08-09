# bj1978 소수 찾기

N = int(input())

sosuLst = list(map(int, input().split()))
result = []

# print(sosuLst)

for i in sosuLst:
    if i == 1:
        pass
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
print(len(result))