import sys
sys.stdin = open("11673in.txt")

def reflect():
    cnt = 0 # 거울 개수 누적할 변수
    dir = 0 # 우방향으로 시작
    nr = nc = 0 # 0,0좌표에서 시작
    # 범위체크
    while 0 <= nr < N and 0 <= nc < N: # 범위 내에 있으면 계속 반복
        if BRD[nr][nc] == 1: # 1번 거울을 만나면
            cnt += 1 # 만난 거울 개수 누적
            # 거울  1 : 방향1 (우->상) (상->우) (좌->하) (하->좌)
            if dir == 0: dir = 1     # 우->상
            elif dir == 1: dir = 0   # 상->우
            elif dir == 2: dir = 3   # 좌->하
            elif dir == 3: dir = 2   # 하->좌
            
        elif BRD[nr][nc] == 2: # 1번 거울을 만나면 방향이면 # 온 방향에 따라 dir 다르다
            # 거울  2 : 방향2 (우->하) (상->좌) (좌->상)  (하->우)    # 방향지정 조건
            cnt += 1 # 만난 거울 개수 누적
            if dir == 0: dir = 3    # 우->하
            elif dir == 1: dir = 2  # 상->좌
            elif dir == 2: dir = 1  # 좌->상
            elif dir == 3: dir = 0  # 하->우
        # 0이든 1이든 2이든(이미 범위 내에 있는 좌표임을 while문에서 검사했음) 한칸 가라 # 앞으로 진행
        nr += dr[dir]
        nc += dc[dir]

    # 범위 벗어나면-->반복문 종료하고 cnt 리턴
    return cnt


# 4방향 델타
dr = [0, -1, 0, 1] # 행  # 우 상 좌 하
dc = [1, 0, -1, 0] # 열

T = int(input())

for tc in range(1, T+1):
    # 격자판 사이즈
    N = int(input())
    # 시작좌표 [0,0]에서 우 ---> 로 진입
    # 거울  1 : 방향1 (우->하) (하->우) (좌->상) (상->좌)   # 방향지정 조건
    # 거울  2 : 방향2 (우->상) (상->우) (하->좌) (좌->하)   # 방향 지정 조건
    # 0은 빈공간 # 1은 방향1 # 2는 방향2
    BRD = [list(map(int, input().split())) for _ in range(N)] # str로 그냥 받아도 되지만... 따옴표 찍기 귀찮으므로
    result = reflect()

    print(f'#{tc} {result}')