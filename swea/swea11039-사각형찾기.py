import sys
sys.stdin = open("11039in.txt")

# 사각형 찾기

# 모든 시작점에서 만들 수 있는 사각형의 경우의 수를 구한다 # 조건을 추가하면 시작점을 추려낼 수 있을지도?(위 1인 경우, 오른쪽 1인 경우, 왼쪽 1인 경우, 아래 1인 경우는 제외....?)

# 시작점 찾기
def search():
    for i in range(N):  # 행
        for j in range(N):  # 열
            if ARR[i][j] == 1:
                start_lst.append([i, j]) # 시작점을 리스트에 저장


# 면적 구하기
def area():
    for start in start_lst: # 시작점 리스트의 시작점을 기준으로 반복
        x = start[0]  # x좌표를 시작점 리스트의 시작점 0번인덱스에 있는 요소로 초기화
        y = start[1]  # y좌표를 시작점 리스트의 시작점 1번인덱스에 있는 요소로 초기화
        w_cnt = 1 # 시작점 기준으로 최소 가로가 1이므로 1로 초기화
        h_cnt = 1 # 시작점 기준으로 최소 세로가 1이므로 1로 초기화

        # 가로 너비 찾기
        while y < N and ARR[x][y + 1] == 1: # y가 범위를 벗어나지 않고 오른쪽 요소가 1이면
            y += 1  # y를 1 늘려서 오른쪽으로 이동
            w_cnt += 1  # 가로 너비를 1 늘린다
            if ARR[x][y + 1] != 1: # 옮겨간 좌표 기준 오른쪽이 1이면
                break  # 가로 변이 끝난 것이므로 반복문 종료

        # 세로 높이 찾기
        if ARR[x + 1][y] == 1: #  현재 x좌표에서 1칸 내려온 자리가 1이면(세로 변이 있으면)
            while x < N and ARR[x + 1][y] == 1:  # x가 범위를 벗어나지 않고 아래쪽 요소가 1이면
                x += 1 # x를 1 늘려서 아래쪽으로 이동
                h_cnt += 1 # 높이를 1 증가시킨다
                if ARR[x + 1][y] != 1: # 옮겨간 좌표 기준 아래쪽이 1이면
                    area_lst.append(w_cnt * h_cnt) # 너비와 높이를 곱한 면적을 리스트에 추가하고
                    break # 반복문 종료
        # else:
        #     area_lst.append(w_cnt * h_cnt) # 없어도 됨 가로세로 너비 1인 경우는 그냥 점이므로....


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    start_lst = []
    area_lst = []

    search()
    area()

    # print(start_lst)
    # print(area_lst)
    print(f'#{tc} {max(area_lst)}')





'''
def search():
    for i in range(N):  # 행
        for j in range(N):  # 열
            if ARR[i][j] == 1:
                start_lst.append([i, j]

def area():
    for start in start_lst:
        x = start[0]
        y = start[1]
        w_cnt = 0
        h_cnt = 0
        while y < N and ARR[x][y] == 1:
            if ARR[x][y+1] == 1:
                y += 1
                w_cnt += 1
            else:
                w_cnt += 1
                break
        if ARR[x+1][y] == 1:
            while x < N and ARR[x][y] == 1:
                if ARR[x+1][y] == 1:
                    x += 1
                    h_cnt += 1
                else:
                    h_cnt += 1
                    area_lst.append(w_cnt*h_cnt)
                    break
        else:
            area_lst.append(w_cnt*h_cnt)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    start_lst = []
    area_lst = []
    search()
    area()
    print(start_lst)
    print(area_lst)
    print(f'#{tc} {max(area_lst)}')
'''