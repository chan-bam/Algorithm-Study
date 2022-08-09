import sys
sys.stdin = open("2669in.txt")

# 100 x 100 2차원배열 0으로 초기화
ARR = [[0]* 100 for _ in range(100)]
# print(ARR)

for n in range(4): # 4개의 4각형 좌표가 입력된다 # 입력받으며 처리
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            ARR[x][y] = 1
sumV = 0
for i in ARR:
    sumV += i.count(1) # 1의 개수 세기
print(sumV)

