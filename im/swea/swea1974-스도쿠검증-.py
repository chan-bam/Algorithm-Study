import sys
sys.stdin = open("1974in.txt")


T = int(input())

# 가로방향 탐색
def verify():
    for i in range(9):
        cnt_h = [0] * 10
        cnt_v = [0] * 10
        for j in range(9):
            cnt_h[sudoku[i][j]] += 1
            cnt_v[sudoku[j][i]] += 1

        for k in range(1, 10): # 1부터 9까지의 카운트배열 검사
            if cnt_h[k] != 1 or cnt_v[k] != 1:
                return 0

        for a in range(0, 9, 3):
            for b in range(0, 9, 3):
                cnt_p = [0] * 10
                for x in range(3): #(r, r+3)
                    for y in range(3): #(c, c+3)
                        cnt_p[sudoku[a+x][b+y]] += 1 #([r][c])
                for u in range(1, 10):
                    if cnt_p[u] != 1:
                        return 0
    return 1



for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {verify()}')