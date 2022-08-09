import sys
sys.stdin = open("1974in.txt")


T = int(input())

# 가로방향 탐색
def horizon():
    for i in range(N):
        judge = []
        for j in range(N): # 가로 한줄 반복
            if sudoku[i][j] not in judge:
                judge.append(sudoku[i][j])
            else:
                return False
    return True

# 세로방향 탐색
def vertical():
    for i in range(N):
        judge = []
        for j in range(N): # 세로 한줄 반복
            if sudoku[j][i] not in judge:
                judge.append(sudoku[j][i])
            else:
                return False
    return True

# 3x3 탐색
def piece():
    for i in range(0, N, 3):     # 시작좌표
        for j in range(0, N, 3):     # 시작좌표
            judge = []
            for k in range(3):   # 이동범위 (3*3)
                for m in range(3):   # 이동범위
                    if sudoku[i+k][j+m] not in judge:
                        judge.append(sudoku[i+k][j+m])
                    else:
                        return False
    return True

def check():
    if horizon():
        if vertical():
            if piece():
                return 1
            else:
                return 0
        else:
            return 0
    return 0

N = 9
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {check()}')