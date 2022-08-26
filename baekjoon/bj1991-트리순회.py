import sys
input = sys.stdin.readline

N = int(input())

def preorder(start):
    if start:
        print(chr(start + 64), end = '')
        preorder(left[start])
        preorder(right[start])

def inorder(start):
    if start:
        inorder(left[start])
        print(chr(start + 64), end = '')
        inorder(right[start])

def postorder(start):
    if start:
        postorder(left[start])
        postorder(right[start])
        print(chr(start + 64), end = '')

# 노드 A ~ Z
left, right = [0] * 27, [0] * 27

for _ in range(N):
    i, j, k = input().split()
    if j != '.':
        left[ord(i) - 64] = ord(j) - 64
    if k != '.':
        right[ord(i) - 64] = ord(k) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)