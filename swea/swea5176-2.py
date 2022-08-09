import sys
sys.stdin = open("5176in.txt")


def inorder(v):
    global value
    if v <= N: # 사용하는 노드의 최대 인덱스는 N
        inorder(v*2) # 왼쪽 자식노드
        tree[v] = value # 중위순회하며 값을 입력
        value += 1 # value값 증가시키기
        inorder(v*2+1) #오른쪽 자식노드


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    # print(tree)
    value = 1
    inorder(1)
    # print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')