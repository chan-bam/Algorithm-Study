
# 조합 # combination

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
N = len(A)   # 4
R = 3    # 몇개를 뽑을지
T = [0] * R
comb(N, R)


print('---------')
res = []

for i in A:
    for j in A:
        res_set = set()
        for k in A:
            if i != j and i != k and j != k:
                res_set.add(i)
                res_set.add(j)
                res_set.add(k)
        res.append(res_set)
for r in res:
    print(r)