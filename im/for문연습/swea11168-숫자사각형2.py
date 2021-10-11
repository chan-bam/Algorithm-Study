import sys
sys.stdin = open("11159in.txt")

# 숫자 사각형 2

T = int(input())

for tc in range(1, T+1):
    # H행 W열
    H, W = map(int, input().split())

    print(f'#{tc}')
    for i in range(H): # 행
        for j in range(1, W*H+1, H): # 열
            print(j+i, end=' ')
        print()
