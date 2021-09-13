# 최빈수 구하기

import sys
sys.stdin = open("1204.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt_lst = [0] * 101 # 점수의 개수를 저장할 count 배열 0으로 초기화

    for i in lst: #lst에 있는 갯수를 첫번째 요소부터 마지막 요소까지 반복하면서
        cnt_lst[i] += 1 # count배열의 일치하는 번지에 1을 추가(갯수 세기)

    maxV = cnt_lst[0] # 가장 큰 count 갯수 찾기, count배열에 저장된 횟수 비교
    for j in range(len(cnt_lst)):
        if maxV <= cnt_lst[j]: # '<='로 해야 뒤에 나오는 것(점수가 높은 것)이 최빈수와 같을때 maxV에 저장됨
            maxV = cnt_lst[j]
            maxP = j # maxV의 번지수(비교한 숫자)를 저장
    print('#{} {}'.format(tc, maxP))