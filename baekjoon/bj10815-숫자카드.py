import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
find_nums = list(map(int, input().split()))

def binary_search(x):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == x:
            return 1
        elif nums[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in find_nums:
    print(binary_search(i), end=' ')