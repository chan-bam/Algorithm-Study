import sys
sys.stdin = open("2304in.txt")

# 기둥의 개수
N = int(input())
        # 위치L, 높이H [L, H]
poles = [list(map(int, input().split())) for _ in range(N)]
poles.sort()
maxV = poles[0][1]

for i in range(len(poles)):
    if maxV < poles[i][1]:
        maxV = poles[i][1]
        maxPos = poles[i][0]
        maxIdx = i # 가장 긴 기둥의 인덱스를 기준으로 나누자


area = 0
higher = poles[0][1]  #초기값
for n in range(1, maxIdx+1): # left
    # 인덱스 마지막 아니면
    # 높이를 비교하여 더 높은 값이 나오면...
    # 기존 H와 * [L2-L1] 해서 누적
    # 인덱스 마지막이면 n == N-2이면.. 새로운 H와 * [L2-L1] 누적
    if higher < poles[n][1]:
        area += (poles[n][0] - poles[n-1][0]) * higher
        higher = poles[n][1]
    else:
        area += (poles[n][0] - poles[n-1][0]) * higher
area += maxV
lower =
for k in range(len(poles), maxIdx, -1):
