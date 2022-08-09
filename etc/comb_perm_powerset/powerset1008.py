# 부분집합 # powerset

# {1, 2, 3}

arr = [1, 2, 3]
N = len(arr)  # 3
A = [0] * N

def powerset(n, k):
    if n == k:
        print(A, end=' ')
        for i in range(n):
            if A[i] == 1:
                print(arr[i], end=' ')
        print()
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)

powerset(N, 0)