import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
# 인접한 두 도시를 연결하는 도로의 길이
distance = list(map(int, input().split())) # N - 1개
# 주유소의 리터당 가격
price = list(map(int, input().split())) # N개

# 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용 출력
cost, minV = 0, sys.maxsize
for i in range(N - 1):
    if price[i] < minV:
        minV = price[i]
    # minV = min(minV, price[i])
    cost += minV * distance[i]
print(cost)


'''
import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
# 인접한 두 도시를 연결하는 도로의 길이
distance = list(map(int, input().split())) # N - 1개
# 주유소의 리터당 가격
price = list(map(int, input().split())) # N개

# 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용 출력
cost, i = 0, 0
while i < N - 1:
    for j in range(i, N - 1):
        if price[i] <= price[j]:
            cost += distance[j] * price[i]
            # print(i, j, cost)
        else:
            i = j
            break
        if j == N - 2:
            print(cost)
            exit(0)
'''