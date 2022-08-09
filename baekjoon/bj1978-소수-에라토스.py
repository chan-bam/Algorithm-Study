M = int(input())
N = int(input())

# 입력범위 10,000 이하의 자연수 : 1 ~ 10,000
# 에라토스테네스의 체

ARR = [True for _ in range(10001)]
ARR[0] = ARR[1] = False # 0과 1은 소수가 아님

for i in range(2, 101): # 2부터 100(10000의 제곱근)까지 숫자의 배수를 False로 바꿔준다
    if ARR[i]: # i가 True이면
        for i in range(i+i, 10001, i):
            ARR[i] = False # 배수를 False로 바꿈

res = []
for s in range(M, N+1):
    if ARR[s] == True:
        res.append(s)

if len(res):
    print(sum(res))
    print(min(res))
else:
    print(-1)