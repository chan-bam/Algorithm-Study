import sys
input = sys.stdin.readline

N = int(input())

D = [0, 1] + [0] * (N - 1)
# D = [0, 1]

for i in range(2, N + 1):
    minV = D[i - 1] + 1
    j = 1
    while j ** 2 <= i:
        minV = min(minV, D[i - j ** 2] + 1)
        j += 1
    D[i] = minV
    # D.append(minV) # 시간 더 오래걸림
print(D[N])


'''
N = int(input())

D = [0, 1]

for i in range(2, N + 1):
    D.append(D[i - 1]) # => D[i]
    j = 1
    while j ** 2 <= i:
        D[i] = min(D[i], D[i - j ** 2])
        j += 1
    D[i] += 1

print(D[N])
'''