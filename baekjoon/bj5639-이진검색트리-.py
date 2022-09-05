import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def post_order(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            mid = i
            break
    post_order(start + 1, mid - 1)
    post_order(mid, end)
    print(tree[start])

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

post_order(0, len(tree) - 1)
