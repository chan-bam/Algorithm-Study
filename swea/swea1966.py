# 1966 숫자를 정렬하자

import sys
sys.stdin = open("1966in.txt")

T = int(input())

for tc in range(1, T+1):
    lenLst = int(input())
    numLst = list(map(int, input().split()))
    # print(numLst)

    # bubble sort # 버블정렬
    for i in range(lenLst-1):
        for j in range(lenLst-i-1): # 뒤에서 i인덱스만큼은 이미 정렬되어있으므로 비교하지 않는다
            if numLst[j] > numLst[j+1]:  # 오름차순정렬이므로 j인덱스(앞 인덱스)가 j+1(뒤 인덱스가) 보다 더 큰 값이 나오면
                numLst[j], numLst[j+1] = numLst[j+1], numLst[j]   # 교환한다

    res = ' '.join(list(map(str, numLst)))
    print(f'#{tc} {res}')



'''
for tc in range(1, T+1):
    lenLst = int(input())
    numLst = list(map(int, input().split()))

    numLst = sorted(numLst)

    sortedLstWrd = ' '.join(list(map(str, numLst)))

    print(f'#{tc} {sortedLstWrd}')
'''