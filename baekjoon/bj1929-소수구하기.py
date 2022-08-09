# 백준 # 1929 # 소수 구하기


# 채점 대박 오래걸리긴 했지만 풀리긴 풀림...

M, N = map(int, input().split())

sosuLst = []

for i in range(M, N+1):
    if i == 1:
        continue
    else:
        for j in range(2, int(i**0.5 + 1)): # 시간 줄이려면...제곱근"까지" 나눠서 소수 판별해보아야함~!!! : 따라서 +1 꼭!!!
                                            # 제곱근-1까지로 하면 결과값에 문제가 있음... 4, 6등등
            if i % j == 0:
                break
        else:
            sosuLst.append(i)

for s in sosuLst:
    print(s)