from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N x N 도시 / M개의 치킨집 고르기
city = [list(map(int, input().split())) for _ in range(N)]
house, chicken = [], []

# 0은 빈칸 # 1은 집 # 2는 치킨집
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:   # 집
            house.append([i, j])
        elif city[i][j] == 2:   # 치킨집
            chicken.append([i, j])

result = sys.maxsize
for pick in combinations(chicken, M):    # 치킨집을 M개 고른 모든 조합
    total = 0
    for x, y in house:    # 집의 좌표
        distance = sys.maxsize
        for i, j in pick:    # 고른 치킨집
            distance = min(distance, abs(i - x) + abs(j - y)) # 집에서 더 가까운 치킨집의 거리
        total += distance    # 도시의 치킨거리는 모든 치킨거리의 합(치킨거리 누적)
    result = min(result, total)    # 도시의 치킨거리의 최소값 구하기

print(result)

# bfs로도 풀 수 있는 문제