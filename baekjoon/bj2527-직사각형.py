import sys
sys.stdin = open("2527in.txt")
def check():
    if (q2 < y1 or y2 < q1) or (p2 < x1 or x2 < p1): # 범위가 안겹치는 경우 # OK
        return 'd'

    # if (x1 == p2 and y2 == q1) or (x2 == p1 and y2 == q1) or (x1 == p2 and y1 == q2) or (x2 == p1 and y1 == q2): # 꼭지점끼리 붙어있는 경우 # OK
    #     return 'c'

    if ((x1 == p2 or x2 == p1) and (y2 == q1 or y1 == q2)): # 꼭지점끼리 붙어있는 경우 # OK
        return 'c'
    if x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1: # 범위가 안겹치는 경우에 해당하지 않고 꼭지점끼리 붙어있는 경우가 아닌 경우 중.. 한 축이 같은 좌표 선상에 놓인 경우 # OK
        return 'b'

    return 'a' # 셋 중 아무것도 아닌 경우

# 좌표의 대소 관계를 비교하여 규칙 찾아내야함
for _ in range(4):
    x1, y1, x2, y2, p1, q1, p2, q2 = map(int, input().split())
    print(check())


# 배열 만들어서 사각형 좌표만큼 인덱스에 입력받으면서 일치하는 패턴 찾는 방식으로 하면 메모리 초과
'''
def search():
    # 2가 나오면 return
    for x in range(N): # 행
        for y in range(M): #열
            if ARR[x][y] == 2:
                return 'a'
            if 0 <= x+1 < N and 0 <= y+1 < M and ARR[x][y] == 1 and ARR[x+1][y] == 1 and ARR[x][y+1] == 0 and ARR[x+1][y+1] == 1:
                return 'b'
            elif 0 <= x+1 < N and 0 <= y+1 < M and ARR[x][y] == 0 and ARR[x+1][y] == 1 and ARR[x][y+1] == 1 and ARR[x+1][y+1] == 0:
                return 'b'
            if 0 <= x+1 < N and 0 <= y+1 < M and ARR[x][y] == 1 and ARR[x+1][y] == 0 and ARR[x][y+1] == 0 and ARR[x+1][y+1] == 1:
                return 'c'
            elif 0 <= x+1 < N and 0 <= y+1 < M and ARR[x][y] == 1 and ARR[x+1][y] == 1 and ARR[x][y+1] == 1 and ARR[x+1][y+1] == 0:
                return 'c'
    return 'd'


rac = [list(map(int, input().split())) for _ in range(4)]

for s in range(4):
    N = 0
    M = 0
    for m in range(8): # range(0, 2, 8) 로 해서 i / i+1 로 구분할 수도 있음
        if m % 2:
            if N < rac[s][m]:
                N = rac[s][m]
        else:
            if M < rac[s][m]:
                M = rac[s][m]
                
    ARR = [[0]*M for _ in range(N)] 
    for i in range(2): 
        for j in range(rac[s][1 + i*4], rac[s][3 + i*4]):
            for k in range(rac[s][0 + i*4], rac[s][2 + i*4]):
                ARR[j][k] += 1

    print(search()) 
    '''