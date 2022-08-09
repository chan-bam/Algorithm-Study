'''
0
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 2
'''

import sys
sys.stdin = open("Ladder1.txt")


T = 10

for tc in range(1, T+1):
    N = int(input())
    BRD  = [list(map(int, input().split())) for _ in range(100)]
    i = 0
    while BRD[99][i] != 2:
        i += 1
    y, x = 99, i # 행, 열
    while y >= 0:
        if x > 0 and BRD[y][x-1] == 1:
            BRD[y][x] = 2
            x = x - 1
        elif 99 > x and BRD[y][x+1] == 1:
            BRD[y][x] = 2
            x = x + 1
        elif BRD[y-1][x] == 1:
            BRD[y][x] = 2
            y = y - 1

    print(f'#{tc} {x}')
'''
    i = 0
    while BRD[99][c] != 2:
        c += 1
    r, c = 99, i # 행, 열

    dr = [0, 0, -1]  # 행  # 우, 좌, 상
    dc = [1, -1, 0]  # 열  
    
    while r > 0:
        for i in range(3)
            nr = r + dr[i]
            nc = c + dc[i]
        if 0 <= nr < 100 and
        if BRD[nr][nc] == 1 and dr[i] == 0: # 새로운 좌표가 1이고... # 좌, 우 방향이면
'''

'''
    while y >= 0:
        y = y - 1
        if x > 0 and BRD[y][x-1] == 1:
            while x > 0 and BRD[y][x-1] == 1:
                x = x - 1
        elif 99 > x and BRD[y][x+1] == 1:
            while 99 > x and BRD[y][x+1] == 1:
                x = x + 1
    print(f'#{tc} {x}')
'''









# def startP():
#     lst = []
#     for i in range(10):
#         if LADDER[0][i] == 1:
#             lst.append(i)
#     return lst

#
# for tc in range(1, T+1):
#     N = int(input())
#     LADDER = [list(map(int, input().split())) for _ in range(10)]
#     stLst = []
#     for s in startP():
#         sp = s
#         i = 0
#         while i <= 9:
#             if LADDER[i][s+1] == 1:
#                 s += 1
#             else:
#                 i += 1
#             if LADDER[i-1][s] == 1:
#                 i
#         if LADDER[i][s] == 2:
#             break
#     print(s)


    # for i in range(10):
    #     while j != 10:
    #         curX = i
    #         curY = j


