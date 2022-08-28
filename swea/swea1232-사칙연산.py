import sys
sys.stdin = open("1232in.txt")

for tc in range(1, 11):
    N = int(input())
    info = [0] + [list(input().split()) for _ in range(N)]
    for i in range(len(info) - 1, 0, -1):
        if len(info[i]) == 4:
            a, b = int(info[int(info[i][2])][1]), int(info[int(info[i][3])][1])
            if info[i][1] == '-':
                info[i] = [i, a - b]
            elif info[i][1] == '+':
                info[i] = [i, a + b]
            elif info[i][1] == '*':
                info[i] = [i, a * b]
            elif info[i][1] == '/':
                info[i] = [i, a // b]

    print(f'#{tc} {info[1][1]}')

'''
import sys
sys.stdin = open("1232in.txt")

def post_order(start):
    if start:
        post_order(left[start])
        post_order(right[start])
        calc(tree[start])

stk = []

def calc(n):
    if str(n) in '-+*/':
        y = stk.pop()
        x = stk.pop()
        if n == '-':
            stk.append(x - y)
        elif n == '+':
            stk.append(x + y)
        elif n == '*':
            stk.append(x * y)
        elif n == '/':
            stk.append(x // y)
    else:
        stk.append(n)

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(N):
        info = list(input().split())
        if len(info) == 4:
            tree[int(info[0])] = info[1]
            left[int(info[0])] = int(info[2])
            right[int(info[0])] = int(info[3])
        else:
            tree[int(info[0])] = int(info[1])

    post_order(1)
    result = stk.pop()
    print(f'#{tc} {result}')
'''