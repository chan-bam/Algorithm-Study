# 중간 평균값 구하기

# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    minV = lst[0]
    maxV = lst[0]
    sumV = 0
    for i in lst:
        if i > maxV:  #최대수 구하기
            maxV = i 
        if i < minV:  #최소수 구하기
            minV = i
        sumV += i # 합계 구하기
    res = (sumV - maxV - minV) / 8  #최대수 최소수 뺀 평균 구하기
    print('#{} {}'.format(tc, int(round(res, 0)))) # 소수점 첫째자리수에서 반올림한 점수