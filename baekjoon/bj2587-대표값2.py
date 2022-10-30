import sys
input = sys.stdin.readline

arr = sorted([int(input()) for _ in range(5)])
print(sum(arr) // 5)
print(arr[2])