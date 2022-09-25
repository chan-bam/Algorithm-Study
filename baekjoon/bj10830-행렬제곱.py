import sys
input = sys.stdin.readline

N, B = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]

def mul(arr1, arr2):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += arr1[i][k] * arr2[k][j]
            res[i][j] %= 1000 # 곱셈, 덧셈에 대한 modulo연산은 분배법칙이 성립된다
    return res

def square(arr, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                arr[i][j] %= 1000 # 입력된 값에도 1000이 넘는 값이 있을 수 있다
        return arr

    temp = square(arr, b // 2) # 재귀 # 분할정복
    if b % 2: # b가 홀수
        return mul(mul(temp, temp), arr)
    else: # b가 짝수
        return mul(temp, temp)

result = square(ARR, B)

for r in result:
    print(*r)