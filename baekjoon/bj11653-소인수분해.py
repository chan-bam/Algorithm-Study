# bj11653 # 소인수분해

# 모든 범위에서 계속 나누기 때문인지 채점 대박 오래걸렸지만......
# (2956ms) 정답이기는 함...?(왜 시간초과 안나지??)

N = int(input())

tmp = N

result = []

i = 2
while i <= N and tmp > 0:
    if tmp % i == 0:
        result.append(i)
        tmp //= i
    if tmp % i != 0:
        i += 1


for r in result:
    print(r)


'''



# 소수 먼저 구하고 소인수분해 -> 시간초과

N = int(input())
tmp = N

sosu = []
# 2부터 N까지 소수 구하기
for i in range(2, N+1):
    for j in range(2, int(i**0.5)+1): # 제곱근까지만 나눠봐도 동일 제곱근 넘어가면 어차피 나눌 수 없게 됨
        if i % j == 0:
            break
    else: # 소수이면
        # 소수 찾았으면 소인수분해
        while tmp % i == 0 and tmp > 0:
            sosu.append(i)
            tmp //= i
    if tmp == 0:
        break

for s in sosu:
    print(s)
# print(sosu)

'''

'''
# 소인수 분해했을때 포함되는 소수를 구함
resSosu = []

for k in sosu:
    if tmp % k == 0:
        while tmp % k == 0 and tmp > 0:
            print(k)
            tmp //= k
# print(resSosu)
'''
'''
# 소인수분해
for m in resSosu:
    while tmp % m == 0 and tmp > 0:
        print(m)
        tmp //= m

'''







'''
# 모든 범위에서 계속 나누기 때문에 채점 대박 오래걸렸지만......
# (2956ms) 정답이기는 함...?(왜 시간초과 안나지??)

N = int(input())

tmp = N

result = []

i = 2
while i <= N and tmp > 0:
    if tmp % i == 0:
        result.append(i)
        tmp //= i
    if tmp % i != 0:
        i += 1

for r in result:
    print(r)
'''