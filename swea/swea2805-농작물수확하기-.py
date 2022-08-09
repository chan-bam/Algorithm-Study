# 2085 농작물 수확하기

# N X N 크기의 농장이 있다
# 농장의 크기는 항상 홀수

import sys
sys.stdin = open("2805.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 농장의 가로 세로 크기
    farm = [list(map(int, input())) for _ in range(N)] # 2차원 배열 입력받음

    benefit = 0 # 합계 누적할 변수 초기화
    for i in range(N):
        mid = N // 2 # 중간 인덱스 구하기
        if i <= mid: # i값이 중간 인덱스와 동일해지기 전까지
            for j in range(mid-i, mid+i+1): # 중간값-i값에서부터 중간값+i값까지 j값의 리스트의 인덱스를 탐색함
                benefit += farm[i][j] # 합계를 누적함
        else:
            for j in range(mid-(N-i-1), mid+(N-i)): # i값이 중간인덱스보다 크면, 중간값 - (전체농장의 크기- i값 -1) 값에서부터 중간값+(전체농장의 크기 -i값) -1 값까지 j값의 인덱스를 탐색함
                benefit += farm[i][j] # 합계를 누적함
    print(f'#{tc} {benefit}')