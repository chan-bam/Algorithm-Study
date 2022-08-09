N = int(input())
A = sorted(list(map(int, input().split())))
M = input()
search = list(map(int, input().split()))

result = ''

# binary search
for s in search:
    front = 0
    rear = N - 1
    while True:
        pivot = (front + rear) // 2
        if front >= rear:
            result += '0'
            break
        if s == A[pivot] or s == A[front] or s == A[rear]:
            result += '1'
            break
        elif s < A[pivot]:
            rear = pivot - 1
        elif s > A[pivot]:
            front = pivot + 1

for r in result:
    print(r)