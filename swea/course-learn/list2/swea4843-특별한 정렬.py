import sys
sys.stdin = open("4843in.txt")

# 선택정렬!!

T = int(input())

for tc in range(1, T+1):
    lenLst = int(input())
    spLst = list(map(int, input().split()))
    # lenLst = len(spLst)

    for i in range(lenLst):
        maxV, minV = 1, 100    # 최대값, 최소값을 저장할 변수를 초기화
        maxP, minP = 0, 0    # 최대값, 최소값의 인덱스값 저장할 변수 초기화
        for j in range(i, lenLst):   # i번째부터 마지막까지를 기준으로
            if i % 2:   # 홀수 인덱스일때
                if minV > spLst[j]:   # 최소값을 구해서
                    minV = spLst[j]   # 최소값 갱신
                    minP = j   # 최소값의 인덱스를 저장
            else:   # 짝수 인덱스일때
                if maxV < spLst[j]:   # 최대값을 구해서
                    maxV = spLst[j]   # 최대값 갱신
                    maxP = j    # 최대값의 인덱스를 저장
        if i % 2: # 홀수 인덱스일때
            spLst[i], spLst[minP] = spLst[minP], spLst[i]    # 가장 작은 값과 i번째 값 교환
        else: # 짝수 인덱스일때
            spLst[i], spLst[maxP] = spLst[maxP], spLst[i]     # 가장 큰 값과 i번째 값 교환

    res = ' '.join(list(map(str, spLst[:10])))     # 10개까지만 출력
    print(f'#{tc} {res}')
