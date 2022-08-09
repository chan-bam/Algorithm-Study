import sys

sys.stdin = open("2628in.txt")

# 가로로 자르는 점선은 높이를 가로지르고
# 세로로 자르는 점선은 너비를 가로지른다 ~~ 헷갈리지 않게 잘 체크!!
# 점선의 위치를 정렬한다
# 규칙 0, w1, w2, ... W <-> 인접한 값들 끼리 차이를 구했을 때 max값끼리 곱하면 최대 면적이 됨!


W, H = map(int, input().split())

w_lst = [0] # 0부터 비교하므로
h_lst = [0]

N = int(input())

for n in range(N):
    kind, line = map(int, input().split())
    if kind == 0:
        w_lst.append(line)
    else:
        h_lst.append(line)
# 오름차순정렬
w_lst.sort()
w_lst.append(H) # 가로점선은 높이를 가로지른다 # 마지막 값으로 높이를 입력함
h_lst.sort()
h_lst.append(W) # 세로점선은 너비를 가로지른다 # 마지막 값으로 너비를 입력함

# 인접한 값의 차이를 구한다
maxW = 0
for i in range(len(w_lst)-1):
    diffW = w_lst[i + 1] - w_lst[i]
    if diffW > maxW:
        maxW = diffW # 차이의 최대값을 구한다

maxH = 0
for j in range(len(h_lst)-1):
    diffH = h_lst[j + 1] - h_lst[j]
    if diffH > maxH:
        maxH = diffH

print(maxW*maxH) # 가로 세로 차이의 최대값을 곱한 값이 면적의 최대값