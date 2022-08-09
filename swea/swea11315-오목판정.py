import sys
sys.stdin = open("11315in.txt")

def five(a, b):
    for d in range(8): # 8방향 델타
        nr = a + dr[d] # 일단 한방향으로 1칸 가라
        nc = b + dc[d] # 일단 한방향으로 1칸 가라

        i = 1   # i조건을 cnt로 대체해서.. while문의 j조건을 삭제하고 cnt == 5일 때 return True해도 됨
        # 조건 순서 중요  # 무조건 범위 먼저 체크해야함!!! # 범위 체크 안하면 벗어난 범위의 인덱스로 인덱스 에러를 일으키거나 잘못된 인덱스(음수인덱스)로 가져와서 조건 단축평가에 의해 False됨
                                                    # 범위 벗어난 인덱스로 먼저 찾으면 안됨!!!
        while i < 5 and 0 <= nr < N and 0 <= nc < N and BRD[nr][nc] == 'o':
            nr += dr[d] # 기존 방향 유지해서 1칸 가라
            nc += dc[d] # 기존 방향 유지해서 1칸 가라
            i += 1
        if i == 5: # i가 5가 되면 반복문에 제한해둔 개수를 True로 다 돌고 나왔다는 의미이므로 오목을 찾은 것임
            return True # True 반환
        # i가 5가 아닌 상태로 반복문을 빠져나왔다면 다시 위의 for문을 실행 --> 방향 전환

    return False # 8 방향 다 돌아봤을때 오목이 없으면 False를 반환

def check():
    for x in range(N):
        for y in range(N):
            if BRD[x][y] == 'o': # 첫번째부터 가로방향 우선으로 'o'가 있는 좌표를 찾아낸다
                if five(x, y) == True:
                    return True # 오목 찾아냈으면 True
    return False # 못찾았으면 False

# 오목은 8방향 다 체크......지만 앞, 위에서부터 흰돌을 다 찾으므로 맞은편은 안봐도 동작함
dr = [1, -1, 0, 0, 1, -1, -1, 1] # 행
dc = [0, 0, 1, -1, -1, 1, -1, 1] # 열

T = int(input())

for tc in range(1, T+1):
    # N x N 오목판
    N = int(input())
    BRD = [list(input()) for _ in range(N)]

    result = "NO"
    if check(): # True이면
        result = "YES"

    print(f'#{tc} {result}')
