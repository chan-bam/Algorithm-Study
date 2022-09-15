import sys
input = sys.stdin.readline

N = int(input())
result = 0
row = [0] * N
visited = [-1] * N

def is_possible(x):
    for i in range(x): # 이전까지 놓은 다른 행 비교
        # 같은 열에 놓인 값이 있는지, 대각선에 놓인 값이 있는지 체크
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False # 있으면 False
    return True # 없으면 True

def n_queen(x):
    global result
    if x == N: # N행 기준 모든 행에 놓았으면 ( == 놓인 개수가 N개이면 )
        result += 1
        return
    for i in range(N):
        row[x] = i # x행, i열 # 현재 열에 행 번호 저장
        if is_possible(x): # 놓을 수 있는 자리인지 체크
            n_queen(x + 1) # 행 + 1 # 다음 행 탐색

n_queen(0)
print(result)




'''
import sys
input = sys.stdin.readline

N = int(input())
row = [0] * N
result = 0

def is_possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queen(x):
    global result
    if x == N:
        result += 1
        return
    for i in range(N):
        row[x] = i
        if is_possible(x):
            n_queen(x + 1)

n_queen(0)
print(result)
'''