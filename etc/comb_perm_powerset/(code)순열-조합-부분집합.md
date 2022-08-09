# 순열

```python
def perm(n, k):
    if n == k:
        print(t)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                t[k] = a[i]
                perm(n, k+1)
                visited[i] = 0

a = [1, 2, 3]
N = len(a)
t = [0] * N
visited = [0] * N
perm(N, 0)
```



# 조합

```python
def comb(n, r):
    if r == 0:
        print(T)
    elif n < r:
        return
    else:
        T[r - 1] = A[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


A = [1, 2, 3, 4]
N = len(A)
R = 3
T = [0] * R
comb(N, R)
```



# 부분집합

```
# {1,2,3} 모든 부분 집합 출력하기
arr = [1, 2, 3]
N = len(arr)
A = [0] * N   # 원소의 포함여부 저장 (0, 1)

def powerset(n, k):         # n: 원소의 갯수, k: 현재depth
    if n == k:              # Basis Part
        print(A, end = ' ')
        for i in range(n):  # 각 부분 배열의 원소 출력
            if A[i] == 1:   # A[i]가 1이면 포함된 것이므로 출력.
                print(arr[i], end=' ')
        print()
    else:                   # Inductive Part
        A[k] = 1            # k번 요소 포함
        powerset(n, k + 1)  # 다음 요소 포함 여부 결정
        A[k] = 0            # k번 요소 미포함
        powerset(n, k + 1)  # 다음 요소 포함 여부 결정

powerset(N, 0)
```



