import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp_p = [0] * N
dp_m = [0] * N

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp_p[i] = max(dp_p[i], dp_p[j] + 1)

for i in range(N - 2, -1, -1):
    for j in range(N - 1, i, -1):
        if nums[i] > nums[j]:
            dp_m[i] = max(dp_m[i], dp_m[j] + 1)
    dp_p[i] += dp_m[i]

print(max(dp_p) + 1)


'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp_p = [0] * N
dp_m = [0] * N
result = 0

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp_p[i] = max(dp_p[i], dp_p[j] + 1)

nums.reverse()

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp_m[i] = max(dp_m[i], dp_m[j] + 1)

dp_m.reverse()

for i in range(N):
    result = max(result, dp_p[i] + dp_m[i] + 1)

print(result)
'''
