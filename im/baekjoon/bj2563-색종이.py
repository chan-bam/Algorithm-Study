import sys
sys.stdin = open("2563in.txt")

# 가로 세로의 크기가 각각 100인 모양인 흰색 도화지
ARR = [[0]*100 for _ in range(100)]

N = int(input()) # 색종이의 수

for n in range(N):
    # 입력되는 값은 좌하단 좌표 (배열로 치면 우상단..?)
    # 붙이는 색종이의 크기는 10X10
    x, y = map(int, input().split())
    for a in range(x, x+10):
        for b in range(y, y+10):
            ARR[a][b] = 1
    res = 0
    for c in ARR:
        res += c.count(1)
print(res)