import sys
sys.stdin = open("1258in.txt")

# 델타 사용할 때 변수명에 주의하자!!!!! dr, dc, nr, nc, r, c

dr = [1, 0]  # 행 # 하 -> 우
dc = [0, 1]  # 열

def square(r, c):
    res = []  # 길이 저장할 리스트 초기화 # [행, 열] # 리턴값
    cnt = 0
    nr, nc = r, c # 초기값은 원래 자리  # nr, nc --- 무의식중에 dr, dc 라고 써서 에러남.... TypeError: 'int' object is not subscriptable
    for x in range(2):  # 방향설정  # 오른쪽이 '0'일때 방향전환
        while 0 <= nr < N and 0 <= nc < N and ARR[nr][nc] != '0':  # 범위 내에 있고 0이 아닐때만 가라
            cnt += 1  # 0이 아닐때 센다 # nr, nc 초기값이 자기자리이므로... # 자기자리부터 개수 센다
            nr += dr[x]  # 이동방향으로 이동
            nc += dc[x]
        nr -= dr[x] # 0으로 넘어가버렸을테니까 초기화...
        nc -= dc[x]
        # 방향 전환할때 입력해줘야한다
        res.append(cnt)  # cnt를 리스트에 입력하고
        cnt = 0  # cnt를 초기화해야함...
    return res # 만들어진 [행,열] 리스트를 리턴한다

def search():
    # 배열 탐색 1열부터
    result = []
    for i in range(1, N):
        for j in range(1, N):
            # 위쪽, 왼쪽이 0이 나오는 경우의 위치를 찾는다
            if ARR[i-1][j] == '0' and ARR[i][j-1] == '0' and ARR[i][j] != '0':
                                                            # 마지막 조건을 안 주면!! 0일때도 좌표를 찾아버린다!!! # 디버깅 힘들었음...
                result.append(square(i, j))  # 함수 실행 # 리턴값 [[행1, 열1], [행2, 열2], ...]
    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 위쪽, 오른쪽에 0을 한줄씩 붙인다
    ARR = [['0'] * (N + 1)] + [['0'] + list(input().split()) for _ in range(N)]
    # print()
    N += 1  # 한자리수 늘어났으니까 범위 조정
    answer = search()

    #####람다#######################################
    # answer.sort(key=lambda x: (x[0] * x[1], x[0])) # 우선순위 1. 행X열 작은순  우선순위2. 행X열 같은 경우 행이 작은 순...
    ###############################################
    # 람다 안쓰고... 정렬할수있을까?

    # 버블소트....
    # 오름차순 정렬 # 앞에있는 게 더 크다면 교환하라..?..

    for k in range(len(answer)-1):
        for u in range(len(answer)-1-k):
            if answer[u][0] * answer[u][1] > answer[u+1][0] * answer[u+1][1]: # 앞에나온거가 더 클 때
                answer[u], answer[u+1] = answer[u+1], answer[u]

            elif answer[u][0] * answer[u][1] == answer[u+1][0] * answer[u+1][1]: # 같을 때
                if answer[u][0] > answer[u+1][0]: # 행값이 더 큰가요...?
                    answer[u], answer[u+1] = answer[u+1], answer[u] # 그렇다면 교환하세요

    # 되네...? 람다 기억안나면 이렇게라도..!!

    print(f'#{tc} {len(answer)}', end=' ')
    for ans in answer:
        print(' '.join(map(str, ans)), end=' ')
    print()