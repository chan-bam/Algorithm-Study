nums = list(map(int, input()))
nums.sort(reverse=True)
print(*nums, sep='')