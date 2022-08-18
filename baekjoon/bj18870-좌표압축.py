import sys
input = sys.stdin.readline

N = int(input())
points = list(map(int, input().split()))
points_sorted = sorted(list(set(points)))
idx_dic = {}

for i in range(len(points_sorted)):
    idx_dic[points_sorted[i]] = i
    # 값을 key로 index값을 item(value)로 저장

for p in points:
    print(idx_dic[p], end=' ')
