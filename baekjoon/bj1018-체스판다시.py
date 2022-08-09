N, M = map(int,input().split())
ARR = [list(map(str,input())) for _ in range(N)]

black_first = [['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B']]

white_first = [['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W']]

cnt_list = []
for row in range(N-8+1): # 행
    for col in range(M-8+1):
        # 8*8 배열 구하기
        cntB = 0
        cntW = 0
        for i in range(8):
            for j in range(8):
                if ARR[row+i][col+j] != black_first[i][j]:
                    cntB += 1
                if ARR[row+i][col+j] != white_first[i][j]:
                    cntW += 1
        cnt_list.append(min(cntB, cntW))
print(min(cnt_list))