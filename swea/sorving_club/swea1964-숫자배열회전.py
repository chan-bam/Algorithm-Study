import sys

sys.stdin = open("1964in.txt")



def reflect(arr):
    return list(zip(*arr))    # 순서가 조금 다름

def rotate90_2(arr):
    rotated = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[i].append(arr[N-j-1][i])
    return rotated

# 배열 회전 연습!!
def rotate90(arr):
    rotated = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[i][j] = arr[N-j-1][i]  # rotated = [[] for _ in range(N)]해서 열마다 append도 가능 -> rotate90_2
    return rotated

def rotate180(arr):
    rotated = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[i][j] = arr[N-i-1][N-j-1]
    return rotated

def rotate270(arr):
    rotated = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[i][j] = arr[j][N-i-1]
    return rotated

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ARR = [list(input().split()) for _ in range(N)]
    ARR90 = rotate90(ARR)
    ARR180 = rotate180(ARR) # 90도 돌린 것을 90도 돌려도 동일한 결과
    ARR270 = rotate270(ARR) # 180도 돌린 것을 90도 돌려도 동일한 결과

    print(f'#{tc}')
    for x in range(N):
        print(''.join(ARR90[x]), end =' ')
        print(''.join(ARR180[x]), end = ' ')
        print(''.join(ARR270[x]), end = ' ')
        print()