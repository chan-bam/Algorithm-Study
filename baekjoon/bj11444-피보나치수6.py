import sys
input = sys.stdin.readline

# 행렬의 거듭제곱 이용 # 분할정복
# n번 째 피보나치 수는 행렬 (1 1, 1 0)^n 의 1행 2열(0행 1열) 값이다(단, n>=1일때)

N = int(input())
P = 1_000_000_007

def mul(arr1, arr2):
    res = [[0] * 2 for _ in range(2)]
    for row in range(2):
        for col in range(2):
            for i in range(2):
                res[row][col] += arr1[row][i] * arr2[i][col]
            res[row][col] %= P
    return res

def square(arr, n):
    if n == 1:
        return arr
    temp = square(arr, n // 2)
    if n % 2: # 홀수이면
        return mul(mul(temp, temp), arr)
    else: # 짝수이면
        return mul(temp, temp)

fib = [[1, 1], [1, 0]] # 거듭제곱할 기준 행렬
# print(square(fib, N))
print(square(fib, N)[0][1])