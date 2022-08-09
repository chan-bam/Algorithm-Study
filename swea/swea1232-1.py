# 사칙연산
# 후위순회

import sys

sys.stdin = open("1232in.txt")

def calc(v):
    if len(tree[v]) == 2: # 트리의 요소값의 길이가 2이면 단말노드
        return int(tree[v][1])
    else:
        L = calc(int(tree[v][2])) # 왼쪽노드 보기
        R = calc(int(tree[v][3])) # 오른쪽노드 보기
        # 가운데에서 연산 처리
        if tree[v][1] == '+':
            return L + R
        elif tree[v][1] == '-':
            return L - R
        elif tree[v][1] == '*':
            return L * R
        elif tree[v][1] == '/':
            return L / R


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for n in range(1, N+1):
        tmp = input().split()
        tree[int(tmp[0])] = tmp
    print(f'#{tc} {int(calc(1))}')
