import sys
input = sys.stdin.readline

# dp

T = int(input().rstrip())

def solve(n):
    cnt0 = [1, 0]
    cnt1 = [0, 1]
    length = len(cnt0)
    if length <= n:
        for i in range(length, n + 1):
            cnt0.append(cnt0[i - 1] + cnt0[i - 2])
            cnt1.append(cnt1[i - 1] + cnt1[i - 2])
    print(cnt0[n], cnt1[n])

for _ in range(T):
    solve(int(input().rstrip()))











'''
   # fi(0) fi(1) fi(2)
cnt0 = [1, 0, 1]
cnt1 = [0, 1, 1]

def fibonacci(n):
    length = len(cnt0)
    if n >= length:
        for i in range(length, n + 1):
            cnt0.append(cnt0[i - 2] + cnt0[i - 1])
            cnt1.append(cnt1[i - 2] + cnt1[i - 1])
    print(cnt0[n], cnt1[n])
    return

T = int(input().rstrip())

for _ in range(T):
    fibonacci(int(input().rstrip()))
'''


'''
def fi(n):
    global cnt0
    global cnt1
    if n == 0:
        cnt0 += 1
        return 0
    elif n == 1:
        cnt1 += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

T = int(input().rstrip())

for t in range(T):
    cnt0 = 0
    cnt1 = 0

    N = int(input().rstrip())
    fi(N)
    print(cnt0, cnt1)
'''