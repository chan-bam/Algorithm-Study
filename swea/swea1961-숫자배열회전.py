import sys
sys.stdin = open("1961in.txt")
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(str, input().split())) for _ in range(N)]
    ARR90 = [lst[::-1] for lst in list(zip(*ARR))] # 행렬뒤집기 90도 방향의 역순으로 되므로... 뒤집어서 저장
    ARR180 = [lst[::-1] for lst in list(zip(*ARR90))]
    ARR270 = [lst[::-1] for lst in list(zip(*ARR180))]

    print(f'#{tc}')
    for res in range(N):
        print(''.join(ARR90[res]), end=' ')
        print(''.join(ARR180[res]), end=' ')
        print(''.join(ARR270[res]), end=' ')
        print()

'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(str, input().split())) for _ in range(N)]
    ARR90 = [lst[::-1] for lst in list(map(list, zip(*ARR)))] # zip함수 튜플로 묶어주므로 리스트로 변환할 때는 이렇게..... 하지만 튜플도 인덱스 접근이 가능하므로 값 변경이 필요한 게 아니라면 큰 의미는X
    ARR180 = [lst[::-1] for lst in list(map(list, zip(*ARR90)))]
    ARR270 = [lst[::-1] for lst in list(map(list, zip(*ARR180)))]

    print(f'#{tc}')
    for res in range(N):
        print(''.join(ARR90[res]), end=' ')
        print(''.join(ARR180[res]), end=' ')
        print(''.join(ARR270[res]), end=' ')
        print()
'''