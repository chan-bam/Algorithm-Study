N = int(input())

maxLen = 0
for num in range(N, 0, -1): # 자신과 같은 수부터 시작해야 에러나지 않음!!! # 1 때문임 # 자기보다 1 적은 숫자로 시작하면 1일때 에러가 날 수 밖에 없는 구조!!
    res = N
    resLst = [N, num]
    while res >= 0:
        res = resLst[-2] - resLst[-1] # 리스트에 저장된 마지막에서 2번째 값에서 마지막 값을 빼준다!!
        if res >= 0:
            resLst.append(res)
        else:
            break
    if maxLen < len(resLst):
        maxLen = len(resLst)
        result = resLst

print(maxLen)
print(*result)