import sys
sys.stdin = open("4839in.txt")


def binarySearch(target):     # target: 찾아야하는 페이지

    left = 1      # 검색 구간의 왼쪽 : 첫번째 페이지 1로 초기화
    right = P     # 검색구간의 오른쪽 : 마지막 페이지 P로 초기화
    center = int((left + right) / 2)  # 중간페이지 찾기

    cnt = 0 # 횟수 카운팅할 변수는 0으로 초기화

    while center != target:   # 중간 페이지가 찾아야하는 페이지가 아닐때 반복
        cnt += 1    # 찾는횟수를 1 늘린다
        if target <= center:   # 찾아야하는 페이지가 중간 페이지보다 앞(작은 페이지)이면 
            right = center    # 오른쪽을 중간 페이지로 바꾼다
        else:   # 찾아야하는 페이지가 중간 페이지보다 뒤(큰 페이지)이면
            left = center     # 왼쪽을 중간페이지로 바꾼다
        center = int((left + right) / 2)   # 중간페이지를 다시 찾는다
    else:    # while조건 처음부터 거짓일때 # 중간페이지가 처음부터 찾는 페이지일때는
        cnt += 1    # 1회 찾은 것이므로 횟수를 늘린다
    return cnt    # 찾은 횟수를 반환한다

T = int(input())

for tc in range(1, T+1):
    # P : 전체 페이지   # Pa : A가 찾을 쪽번호   # Pb : B가 찾을 쪽번호 Pb
    P, Pa, Pb = map(int, input().split())

    cntA = binarySearch(Pa)   # A가 페이지를 찾는 횟수를 구함
    cntB = binarySearch(Pb)   # B가 페이지를 찾는 횟수를 구함

    if cntA < cntB:
        vic = 'A'   # 이긴사람 A를 반영
    elif cntA > cntB:
        vic = 'B'   # 이긴사람 B를 반영
    else:
        vic = 0    # 무승부는 0

    print(f'#{tc} {vic}')
