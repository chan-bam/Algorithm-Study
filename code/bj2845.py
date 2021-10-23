L, P = map(int, input().split())
people = list(map(int, input().split()))
LP = L * P
for p in people:
    print(p - LP, end=" ")