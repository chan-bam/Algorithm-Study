import sys
sys.stdin = open("11159in.txt")

# 숫자 사각형 2

T = int(input())

for tc in range(1, T+1):
    # H행 W열
    H, W = map(int, input().split())
    print(f'#{tc}')
    for i in range(H): # 행
        if i % 2 == 0:
            for j in range(1, W + 1): # 열
                print(j + i * W, end=' ')
        else:
            for j in range(W, 0, -1):
                print(j + i * W, end=' ')
        print()