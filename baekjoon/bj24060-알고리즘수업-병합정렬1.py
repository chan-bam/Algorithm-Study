import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = (len(arr) + 1) // 2 # !!

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    arr2 = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr2.append(left[i])
            result.append(left[i])
            i += 1
        else:
            arr2.append(right[j])
            result.append(right[j])
            j += 1

    while i < len(left):
        arr2.append(left[i])
        result.append(left[i])
        i += 1
    while j < len(right):
        arr2.append(right[j])
        result.append(right[j])
        j += 1
    return arr2

result = []
merge_sort(A)
# print(result)
if len(result) < K:
    print(-1)
else:
    print(result[K - 1])



'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = (len(arr) + 1) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j = 0, 0
    arr2 = []
    # 두개의 정렬된 리스트를 합병하는 단계 # 실제 정렬이 이루어지는 시점
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr2.append(left[i])
            result.append(left[i])
            i += 1
        else:
            arr2.append(right[j])
            result.append(right[j])
            j += 1
    while i < len(left):
        arr2.append(left[i])
        result.append(left[i])
        i += 1
    while j < len(right):
        arr2.append(right[j])
        result.append(right[j])
        j += 1
    return arr2

result = []
merge_sort(A)

if len(result) < K:
    print(-1)
else:
    print(result[K - 1])
'''