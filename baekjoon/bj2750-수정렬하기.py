N = int(input())
# nums = [int(input()) for _ in range(N)]
'''
nums.sort()
'''

'''
# bubble sort
for i in range(N - 1):
    for j in range(N - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
'''

'''
# selection sort
for i in range(N - 1):
    min = 1000
    idx = i
    for j in range(i + 1, N):
        if nums[idx] > nums[j]:
            idx = j
    if i != idx:
        nums[i], nums[idx] = nums[idx], nums[i]
'''

# print(*nums, sep='\n')

# counting sort
cnt = [0 for _ in range(2002)]

for _ in range(N):
    cnt[int(input()) + 1001] += 1

for i in range(len(cnt)):
    if cnt[i]:
        print(i - 1001)

