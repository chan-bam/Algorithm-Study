import sys
sys.stdin = open("5174in.txt")

def inorder(v):
    global cnt
    if v != 0: # 노드번호 v가 0이 아닐때까지만 실행 # 0이면 종료
        inorder(tree[v][0]) # 왼쪽 자식 보기
        cnt += 1
        inorder(tree[v][1]) # 오른쪽 자식 보기


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[0, 0] for _ in range(E+2)]
    tmp = list(map(int, input().split()))
    for i in range(0, len(tmp), 2):
        if tree[tmp[i]][0]:
            tree[tmp[i]][1] = tmp[i+1]
        else:
            tree[tmp[i]][0] = tmp[i+1]
    # print(tree)
    cnt = 0
    inorder(N)
    print(f'#{tc} {cnt}')