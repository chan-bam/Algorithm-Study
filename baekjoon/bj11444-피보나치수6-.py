import sys
input = sys.stdin.readline

def mul(arr1, arr2):
    res = [[0] * 2 for _ in range(2)]
    for col in range(2):
        for row in range(2):
            e = 0
            for i in range(2):
                e += arr1[col][i] * arr2[i][row]
            res[col][row] = e % P
    return res

def square(n, arr):
    if n == 1:
        return arr
    temp = square(n // 2, arr)
    if n % 2:
        return mul(mul(temp, temp), arr)
    else:
        return mul(temp, temp)

N = int(input())
P = 1_000_000_007
fib = [[1, 1], [1, 0]]
print(square(N, fib)[0][1])
