import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(R)]

dx_t = [0, -1, 0, 1]
dx_b = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(R):
    if ARR[i][0] == -1:
        t, b = i, i + 1
        break

def dust(x, y):
    amount = ARR[x][y] // 5
    for i in range(4):
        nx, ny = x + dx_t[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and ARR[nx][ny] != -1:
            ARR2[nx][ny] += amount
            ARR[x][y] -= amount

def clean(start, dx):
    x, y = start, 1
    i = 0
    temp1 = ARR[x][y]
    ARR[x][y] = 0
    while True:
        x, y = x + dx[i], y + dy[i]
        if x < 0 or R <= x or y < 0 or C <= y:
            x, y = x - dx[i], y - dy[i]
            i = (i + 1) % 4
            x, y = x + dx[i], y + dy[i]
        if ARR[x][y] == -1:
            return
        temp2 = ARR[x][y]
        ARR[x][y] = temp1
        temp1 = temp2

for _ in range(T):
    ARR2 = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if ARR[i][j] != -1 and ARR[i][j]:
                dust(i, j)

    for i in range(R):
        for j in range(C):
            ARR[i][j] += ARR2[i][j]

    clean(t, dx_t)
    clean(b, dx_b)

result = 0

print(sum(map(sum, ARR)) + 2)

'''
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

ARR = [list(map(int, input().split())) for _ in range(R)]

dx_t = [0, -1, 0, 1]
dx_b = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dust(x, y):
    amount = ARR[x][y] // 5
    for i in range(4):
        nx, ny = x + dx_t[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and ARR[nx][ny] != -1:
            ARR2[nx][ny] += amount
            ARR[x][y] -= amount

def clean(start, dx):
    x, y = start, 1
    i = 0
    temp1 = ARR[x][y]
    ARR[x][y] = 0
    while True:
        x, y = x + dx[i], y + dy[i]
        if x < 0 or R <= x or y < 0 or C <= y:
            x, y = x - dx[i], y - dy[i]
            i = (i + 1) % 4
            x, y = x + dx[i], y + dy[i]
        if ARR[x][y] == -1:
            return
        temp2 = ARR[x][y]
        ARR[x][y] = temp1
        temp1 = temp2

for _ in range(T):
    ARR2 = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if ARR[i][j] != -1 and ARR[i][j]:
                dust(i, j)

    for i in range(R):
        for j in range(C):
            ARR[i][j] += ARR2[i][j]

    for i in range(R):
        if ARR[i][0] == -1:
            clean(i, dx_t)
            clean(i + 1, dx_b)
            break 
            
result = 0
for a in ARR:
    result += sum(a)
print(result + 2)
'''

'''
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

ARR = [list(map(int, input().split())) for _ in range(R)]

def dust(x, y):
    amount = ARR[x][y] // 5
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 4방향
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and ARR[nx][ny] != -1: # 유효한 범위 내이고 공기청정기가 아니면
            ARR2[nx][ny] += amount # 확산된 양 누적
            ARR[x][y] -= amount # 확산된 양만큼 기존 좌표 미세먼지 감소

def top(start):
    # 우 상 좌 하
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y = start, 1
    i = 0
    temp1 = ARR[x][y]
    ARR[x][y] = 0
    while True:
        x, y = x + dx[i], y + dy[i]
        if x < 0 or R <= x or y < 0 or C <= y:
            x, y = x - dx[i], y - dy[i]
            i = (i + 1) % 4
            x, y = x + dx[i], y + dy[i]
        if ARR[x][y] == -1:
            break
        temp2 = ARR[x][y]
        ARR[x][y] = temp1
        temp1 = temp2

def bottom(start):
    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = start, 1
    i = 0
    temp1 = ARR[x][y]
    ARR[x][y] = 0
    while True:
        x, y = x + dx[i], y + dy[i]
        if x < 0 or R <= x or y < 0 or C <= y:
            x, y = x - dx[i], y - dy[i]
            i = (i + 1) % 4
            x, y = x + dx[i], y + dy[i]
        if ARR[x][y] == -1:
            break
        temp2 = ARR[x][y]
        ARR[x][y] = temp1
        temp1 = temp2

for _ in range(T):
    ARR2 = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if ARR[i][j] != -1:
                dust(i, j) # 확산

    for i in range(R):
        for j in range(C):
            ARR[i][j] += ARR2[i][j]

    for i in range(R):
        if ARR[i][0] == -1:
            top(i)
            bottom(i + 1)
            break # !!!!!

result = 0
for a in ARR:
    result += sum(a)
print(result + 2) # 공기청정기 2대 -1-1 == -2 빼야함
'''