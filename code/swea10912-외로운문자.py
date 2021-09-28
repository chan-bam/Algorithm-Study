# 10912 외로운문자

import sys
sys.stdin = open("10912.txt")

T = int(input())

for tc in range(1, T+1):
    wrd = input() 
    wrdDic = {}    # 빈 딕셔너리 생성
    for w in wrd:   # 문자별로 비교
        if w not in wrdDic:
            wrdDic[w] = 1    # 딕셔너리에 문자열 없으면 초기값 1 넣어줌
        else:
            wrdDic[w] += 1   # 딕셔너리에 문자열 있으면 +1 값 누적
    resLst = []   #결과 문자열 반환 리스트
    for key, val in wrdDic.items():
        if val % 2:   # val값이 홀수이면
            resLst.append(key)   #결과 문자열 반환 리스트에 문자열 추가해준다
    if len(resLst):
        resWrd = ''.join(sorted(resLst))  # 정렬해서 문자열로 출력한다
        print(f'#{tc} {resWrd}')
    else:
        print(f'#{tc} Good')  # 결과 문자열의 길이가 0 이면 모두 짝이 맞으므로 Good을 출력해준다