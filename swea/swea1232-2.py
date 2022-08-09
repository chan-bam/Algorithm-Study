#swea #1232 #사칙연산

import sys
sys.stdin = open("1232in.txt")

def postorder(v):
    if len(tree[v]) == 1:
        return int(tree[v][0])
    else:
        L = postorder(int(tree[v][1]))
        R = postorder(int(tree[v][2]))

        if tree[v][0] == '-':
            return L-R
        elif tree[v][0] == '+':
            return L+R
        elif tree[v][0] == '*':
            return L*R
        else:
            return L/R

T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(1, N+1):
        tmp = input().split()
        tree[int(tmp[0])] = tmp[1:4]
    # print(tree)

    print(f'#{tc} {int(postorder(1))}')
