import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split())) # N개

start, end = 0, max(trees)

while start <= end:
    # print(start, end)
    middle = (start + end) // 2
    height = 0
    for tree in trees:
        if tree > middle:
            height += (tree - middle)
    if height >= M:
        start = middle + 1
    else:
        end = middle - 1
print(end)

# 시간초과
#
# trees.sort()
#
# for cut in range(trees[0], 1, -1):
#     height = 0
#     for tree in trees:
#         if tree > cut:
#             height += (tree - cut)
#     if height >= M:
#         break
# print(cut)