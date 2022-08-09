import sys
sys.stdin = open("11718in.txt")

# 초기화와 반복문의 위치를 조건에 따라 잘 설정해줘야한다..!!!

def catch(r, c):
    cnt = 0 # 토끼의 개수를 누적할 변수
    for k in range(8): # 8방향 탐색
        for u in range(1, N+1):
            nr = r + dr[k]*u # 단순 8방향 탐색은 이 구조가 더 간단!!! # 초기화와 인덱스 이동을 한번에 할수있어서...
            nc = c + dc[k]*u # 탐색 기준 위치가 정해져있으므로 기준위치를 기준으로 범위만큼 떨어진 위치로 탐색하게 하는 방법
            # 델타로 이동한 위치의 범위 체크
            if 0 <= nr < N and 0 <= nc < N and ARR[nr][nc] != 0: # 범위 안벗어나면
                if ARR[nr][nc] == '2': # 토끼면  # 테스트케이스 구조상 사냥꾼이 같은 토끼를 잡는 경우는 없으므로 그대로 둬도 무방
                    cnt += 1 # 카운트를 증가시켜라
                elif ARR[nr][nc] == '3' or '1': # 바위면
                    break # 해당방향 이동 중지
                # elif ARR[nr][nc] == "1": # 사냥꾼이면 # 테스트케이스상 사냥꾼이 사냥꾼을 사격할 수 있는 케이스는 없는듯..?
                #     break # 해당 방향 이동 중지
            else: # 범위 벗어나면 반복문 종료 # 사실 범위 벗어나도 위에 조건문에 의해 탐색은 안하긴 함..
                break
    return cnt

def hunt():
    totalCnt = 0
    for i in range(N):
        for j in range(N):
            if ARR[i][j] == '1': # 사냥꾼이면
                totalCnt += catch(i, j)
    return totalCnt # 반복문 다 돌면 함수 종료

# 8방향 델타
dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]

T = int(input())

for tc in range(1, T+1):
    # N X N 배열
    N = int(input())

    ARR = [list(input().split()) for _ in range(N)]

    result = hunt()

    print(f'#{tc} {result}')