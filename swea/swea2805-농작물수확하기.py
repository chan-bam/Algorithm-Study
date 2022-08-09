import sys
sys.stdin = open("2805in.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    FARM = [list(map(int, input())) for _ in range(N)]
    # print(FARM)
    sumV = 0
    mid = N//2

    for i in range(N):
        if i <= mid:
            sumV += sum(FARM[i][mid-i:N-(mid-i)])
        else:
            sumV += sum(FARM[i][i-mid:N-(i-mid)])

    print(f'#{tc} {sumV}')

'''
import sys
sys.stdin = open("2805in.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    FARM = [list(map(int, input())) for _ in range(N)]
    # print(FARM)
    sumV = 0

    for i in range(N):
        if i <= (N//2):
            for j in range(N//2-i, N-(N//2-i)):
                sumV += FARM[i][j]
        else:
            for j in range(i-N//2, N-(i-N//2)):
                sumV += FARM[i][j]

    print(f'#{tc} {sumV}')
'''