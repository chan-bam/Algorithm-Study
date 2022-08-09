M = int(input())
N = int(input())

sosuLst = []

for i in range(M, N+1):
    for j in range(1, int(i**0.5)+1): # i-1까지 해도 되지만... 제곱근까지만 찾아도 소수 유무를 판단할 수 있다
        if j == 1:
            continue
        elif i % j == 0:
            break
    else:
        if i != 1:
            sosuLst.append(i)

if len(sosuLst):
    # print(sosuLst)
    print(sum(sosuLst))
    print(min(sosuLst))
else:
    print(-1)