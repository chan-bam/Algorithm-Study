import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        dist1 = ((x1 - cx)**2 + (y1 - cy)**2)**0.5 < r
        dist2 = ((x2 - cx)**2 + (y2 - cy)**2)**0.5 < r
        if dist1 and dist2:
            continue
        elif dist1 or dist2:
            cnt += 1
    print(cnt)
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        dist1 = ((x1 - cx)**2 + (y1 - cy)**2)**0.5
        dist2 = ((x2 - cx)**2 + (y2 - cy)**2)**0.5
        if dist1 < r and dist2 < r:
            continue
        elif dist1 < r or dist2 < r:
            cnt += 1
    print(cnt)
'''