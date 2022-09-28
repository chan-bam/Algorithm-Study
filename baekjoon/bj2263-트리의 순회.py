import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    print(root, end=' ')

    left_node = in_idx[root] - in_start # 왼쪽 서브트리 노드의 개수
    right_node = in_end - in_idx[root] # 오른쪽 서브트리 노드의 개수

    pre_order(in_start, in_start + left_node - 1, post_start, post_start + left_node - 1)
    pre_order(in_end - right_node + 1, in_end, post_end - right_node, post_end - 1)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
in_idx = [0] * (n + 1)

for i in range(n):
    in_idx[in_order[i]] = i # in_order의 index값 저장

pre_order(0, n - 1, 0, n - 1)

'''
6
4 2 5 1 6 3
4 5 2 3 6 1
1 2 4 5 6 3 

15
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
1 2 4 8 9 5 10 11 3 6 12 13 7 14 15

4
1 2 3 4
4 3 2 1
1 2 3 4

4
4 3 2 1
4 3 2 1
1 2 3 4


11
8 4 2 5 9 1 10 6 3 7 11
8 4 9 5 2 10 6 11 7 3 1
1 2 4 8 5 9 3 6 10 7 11


21
8 14 4 15 9 16 2 17 10 5 1 6 11 18 3 19 12 20 7 21 13
14 8 15 16 9 4 17 10 5 2 18 11 6 19 20 12 21 13 7 3 1
'''

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 이진 검색 트리(백준5639)와 유사한 문제

N = int(input())
in_order = list(map(int, input().split())) # 중위 순회
post_order = list(map(int, input().split())) # 후위 순회

def pre_order(in_start, in_end, post_start, post_end):
    # 역전되면 구분할 노드가 없는 것
    if in_start > in_end or post_start > post_end:
        return

    # 루트
    root = post_order[post_end]
    print(root, end = ' ')

    left = idx[root] - in_start     # 중위순회의 루트 왼쪽 개수 : 왼쪽 서브트리의 노드 개수 구하기
    right = in_end - idx[root]    # 중위순회의 루트 오른쪽 개수 : 오른쪽 서브트리의 노드 개수 구하기

    # 서브트리의 개수를 기준으로 서브트리의 인덱스를 구할 수 있음
    # 왼쪽 서브트리
    pre_order(in_start, in_start + left - 1, post_start, post_start + left - 1)
    # 오른쪽 서브트리
    pre_order(in_end - right + 1, in_end, post_end - right, post_end - 1)

idx = [0] * (N + 1)

# 후위순회의 끝 값이 중위순회의 어디 인덱스에 위치했는지 확인을 위해
# 중위순회의 값들의 인덱스값을 저장
for i in range(N):
    idx[in_order[i]] = i

pre_order(0, N - 1, 0, N - 1)

'''