import sys

sys.stdin = open("2527in.txt")

for i in range(4):
    x1, y1, p1, q2, x2, y2, p2, q2 = map(int, input().split())

# 수학적인 조건을 잘 찾아보자..


# 배열에 다 채워서 조건 비교 하니 시간초과가.....
'''
def search():
    # 2가 나오면 return
    for x in range(N): # 행
        for y in range(M): #열
            if ARR[x][y] == 2:
                return 'a'
            if 0 <= x+1 < N and 0 <= y+1 < M and ARR[x][y] == 1 and ARR[x+1][y] == 1 and ARR[x][y+1] == 0 and ARR[x+1][y+1] == 1:
                return 'b'
            elif 0 <= x+1 < N and 0 <= y+1 < M and ARR[x][y] == 0 and ARR[x+1][y] == 1 and ARR[x][y+1] == 1 and ARR[x+1][y+1] == 1:
                return 'b'
            if 0 <= x+1 < N and 0 <= y+1 < M and ARR[x][y] == 1 and ARR[x+1][y] == 0 and ARR[x][y+1] == 0 and ARR[x+1][y+1] == 1:
                return 'c'
            elif 0 <= x+1 < N and 0 <= y+1 < M and ARR[x][y] == 0 and ARR[x+1][y] == 1 and ARR[x][y+1] == 1 and ARR[x+1][y+1] == 0:
                return 'c'
    return 'd'

# 4개의 줄
rac = [list(map(int, input().split())) for _ in range(4)]

for s in range(4):
    # 행 중에서 가장 큰 값, 열 중에서 가장 큰 값을 찾아서...
    N = 0
    M = 0
    for m in range(0, 8, 2):
        if N < rac[s][m+1]:
            N = rac[s][m+1]
        if M < rac[s][m]:
            M = rac[s][m]
    # print(N, M)

    # 2차원 배열만들기
    ARR = [[0]*M for _ in range(N)] # 가장 큰 값으로
    for i in range(2): # 두번 반복
        for j in range(rac[s][1 + i*4], rac[s][3 + i*4]):
            for k in range(rac[s][0 + i*4], rac[s][2 + i*4]):
                ARR[j][k] += 1

    print(search()) # 사각형의 종류 찾기
'''