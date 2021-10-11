import sys
sys.stdin = open("11183in.txt")

# 정올 1338 풀이 참조

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(1, N + 1):  # 높이 N까지
        k = N + 1     # 다른 코드 참조
        p = 0       # 다른 참조
        print(' ' * (N - i + 1), end='') # 공백의 개수 결정
        for j in range(1, i + 1):
            print(chr(64+(p+i)%26), end = ' ')      # 다른 코드 참조
            k = k - 1    # 다른 코드 참조
            p = p + k    # 다른 코드 참조
        print()