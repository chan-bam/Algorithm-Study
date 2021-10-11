import sys
sys.stdin = open("1220in.txt")

# 이 문제의 핵심은..
# 1. 문제 파악 >> 지문이 다소 혼란스럽게 나와있음 : 침착한 문제 파악이 필요
# 2. 1 밑에 2가 교차로 나왔을 때만 개수를 세는 것
    # 중요한 것은 플래그 비트 !! ->

T = 10

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    # print(table)

    cnt = 0
    for i in range(N): # 행
        flag = 0
        for j in range(N): # 열
            if table[j][i] == 1 and flag == 0: # 나올 수 있는 경우가 3가지인데 0이 나오면 아무것도 하지 않고 2가 나오면 어차피 0으로 초기화해주므로.. # tmp == 0 인 부분은 굳이 체크하지 않아도 동작함
                flag = 1
            if table[j][i] == 2 and flag == 1: # tmp가 1일때만 개수를 세라 # 교차해서 나와야 하므로
                flag = 0 # 그리고 tmp를 0으로 바꿔라..... 다시 밑에서 n이 나와야 s의 개수를 세므로! # s가 나오면 숫자 안 세도록!!!
                cnt += 1

    print(f'#{tc} {cnt}')