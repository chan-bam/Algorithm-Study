# 1946. 간단한 압축 풀기

import sys
sys.stdin = open("1946.txt")

T = int(input()) # 테스트케이스 갯수 입력

for tc in range(1, T+1):    # 테스트케이스 개수만큼 반복
    N = int(input())   # 들어오는 알파벳의 종류의 갯수
    wrd = ''    # 빈 문자열 초기화
    for z in range(N):   # 알파벳 종류 갯수만큼 반복
        Ci, Ki = map(str, input().split()) # 알파벳, 갯수 입력
        wrd += Ci*int(Ki)  # 문자열에 (알파벳*갯수) 추가
    print(f'#{tc}')  # 테스트케이스 번호 출력
    for w in range(len(wrd)):  # 문자열 길이만큼 반복하여 인덱스 접근
        if (w+1) % 10 == 0:   # (인덱스번호+1)을 10으로 나눈 나머지가 0이면
            print(wrd[w])   # 해당 인덱스의 문자열을 출력하고 줄바꿈
        else:   # (인덱스번호+1)을 10으로 나눈 나머지가 0이 아니면
            print(wrd[w], end='')  # 해당 인덱스의 문자열을 "줄바꿈 없이" 출력
    print() # 모든 문자열을 출력하고 for문 빠져나왔으면 줄바꿈하기

    # 슬라이싱으로 출력도 가능
    # 슬라이싱은 범위를 벗어나도 출력이 가능하다
