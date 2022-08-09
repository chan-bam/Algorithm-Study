import sys
sys.stdin = open("2578in.txt")

def check():
    total = 0
    cntC = cntD = 0
    for a in range(5):
        cntA = cntB = 0
        for b in range(5):
            if bingo[a][b] == '*':
                cntA += 1
            if bingo[b][a] == '*':
                cntB += 1
        if cntA == 5:
            total += 1
        if cntB == 5:
            total += 1

        if bingo[a][a] == '*': # / 대각선
            cntC += 1
        if bingo[a][4-a] == '*': # \ 대각선
            cntD += 1

    if cntC >= 5:
        total += 1
    if cntD >= 5:
        total += 1

    return total

def game():
    for u in range(len(mc)):
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == mc[u]:
                    bingo[i][j] = '*'
                    if check() >= 3:
                        return u+1


# 빙고판은 2차원 배열로
bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 불러주는 수는 1차원배열로
mc = []
for m in range(5):
    for k in input().split():
        mc.append(int(k))
print(game())