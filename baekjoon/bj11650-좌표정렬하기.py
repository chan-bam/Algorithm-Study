N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]
points.sort()

for i in points:
    print(*i)