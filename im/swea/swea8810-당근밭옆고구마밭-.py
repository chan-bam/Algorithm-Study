import sys

sys.stdin = open("8810in.txt")
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    goguma = list(map(int, input().split())) + [0] # 마지막 값으로 0을 추가해서 마지막에는 무조건 동일하거나 감소하도록....
                                                   # 0은 고구마개수의 최소값으로 값을 찾아내는데 지장은 없지만 -1처럼 아예 범위를 벗어나는 값으로 설정하면 더 명확할듯
    # print(goguma)

    cntV = 0 # 큰 고구마줄기의 개수 세기
    sumV = goguma[0] # 맨 처음 값으로 합계값 초기화
    g_cnt = 1 # 맨 처음 한개 미리 세고 시작
    maxG = 0 # 가장 긴 값 저장
    maxS = 0 # 가장 긴 값의 합의 최대값 저장

    for i in range(1, N+1):  # 0을 붙였으므로 인덱스 N까지임에 주의.....!!!!!!!! # range(1, N)으로 하면 잘못된 값 나온다
        if goguma[i-1] < goguma[i]: # 전값보다 증가했으면
            sumV += goguma[i] # 합계 누적하기
            g_cnt += 1 # 길이 세는 변수 늘리기

        else: # 전값보다 감소했으면
            if g_cnt > 1: # 길이가 1 이상일 때만 영역으로 본다
                cntV += 1 #영역의 개수 늘리기
                # 영역의 개수 셌으니 영역 길이 및 합의 최대값 비교 및 갱신
                if g_cnt > maxG:
                    maxG = g_cnt
                    maxS = sumV
                elif g_cnt == maxG:
                    if maxS < sumV:
                        maxS = sumV
            if i == N: # 인덱스 마지막이면..  # 마지막값으로 -1로 넣고 -1이 나왔을 때 종료하도록 해도 괜찮을듯..(마지막값)
                break # 반복문 종료하라
            else: # 마지막 아니면
                sumV = goguma[i]  # 합계값의 초기값 변경
                g_cnt = 1 # 영역 길이의 초기값 변경
    print(f'#{tc} {cntV} {maxS}')