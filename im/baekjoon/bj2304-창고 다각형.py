import sys
sys.stdin = open("2304in.txt")

'''
7
2 10
11 4
4 6
5 3
8 10
13 10
15 10
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''
# 기둥의 개수
N = int(input())
        # 위치L, 높이H [L, H]
poles = [list(map(int, input().split())) for _ in range(N)]
poles.sort()

maxV = maxV2 = -1 # 첫번째부터 최대값 나올 수 있으므로....

for i in range(len(poles)):
    if maxV < poles[i][1]:
        maxV = poles[i][1]
        maxPos = poles[i][0]
        maxIdx = i # 첫번째 나오는 가장 긴 기둥의 인덱스
    if maxV <= poles[i][1]:
        maxPos2 = poles[i][0]
        maxIdx2 = i # 마지막 나오는 가장 긴 기둥의 인덱스

area = 0
# 왼 - > 가장 높은 기둥의 첫번째 인덱스
higher = poles[0][1]  #초기값
for n in range(1, maxIdx+1): # left
    # 높이를 비교하여 더 높은 값이 나오면...
    # 기존 H와 * [L2-L1] 해서 누적
    if higher < poles[n][1]:
        area += (poles[n][0] - poles[n-1][0]) * higher
        higher = poles[n][1]
    else:
        area += (poles[n][0] - poles[n-1][0]) * higher

# 오 - > 가장 높은 기둥의 마지막 인덱스
higher2 = poles[-1][1]  #초기값
for k in range(len(poles)-2, maxIdx2-1, -1):
    # 높이를 비교하여 더 높은 값이 나오면...
    # 기존 H와 * [L2-L1] 해서 누적
    if higher2 < poles[k][1]:
        area += (poles[k+1][0] - poles[k][0]) * higher2
        higher2 = poles[k][1]
    else:
        area += (poles[k+1][0] - poles[k][0]) * higher2

area += (maxPos2 +1 - maxPos) * maxV  # (가장 높은 기둥의 마지막 위치 + 1 - 가장 높은 기둥의 첫번재 위치) * 최대높이

print(area)