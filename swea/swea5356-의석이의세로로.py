import sys
sys.stdin = open("5356in.txt")

T = int(input())

for tc in range(1, T+1):
    # 테스트케이스는 총 다섯 줄
    ARR = [list(input()) for _ in range(5)]
    print(f'#{tc} ', end='')


    for x in range(15): # 열은 최대 15줄
        for y in range(5): # 행은 5줄(고정)
            try: # 에러없으면
                print(ARR[y][x], end = '')
            except: # 인덱스에러나면!!!
                print('', end = '')
    print()