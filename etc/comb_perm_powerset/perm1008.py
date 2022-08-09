
# 순열  # permutation

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
N = len(a)   # 3
t = [0] * N
visited = [0] * N
perm(N, 0)
