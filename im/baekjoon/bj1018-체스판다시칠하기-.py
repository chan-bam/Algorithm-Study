
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
BRD = [list(input()) for _ in range(N)]
min_cnt = 50 * 50
STD = [['B', 'W']*4, ['W', 'B']*4]

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        W_cnt = 0  # 첫번째가 W로 시작하는 경우
        B_cnt = 0  # 첫번째가 B로 시작하는 경우
        for x in range(8):
            for y in range(8):
                # 한줄씩 비교
                # 짝수행 홀수행일때 시작값 다름
                if BRD[i+x][j+y] != STD[x%2][y]: # 짝수행일때 0번인덱스 #홀수행일때 1번인덱스 값 가져오도록...
                    B_cnt += 1
                if BRD[i+x][j+y] != STD[(x+1)%2][y]: # 짝수행일때 1번인덱스 #홀수행일때 0번인덱스 값 가져오도록...
                    W_cnt += 1
        min_cnt = min(min_cnt, W_cnt, B_cnt)
print(min_cnt)
'''
import sys
sys.stdin = open("1018in.txt")
input = sys.stdin.readline
T = int(input())

for tc in range(T):
    # N*M 크기의 보드
    # 8*8크기의 체스판
    N, M = map(int, input().split())
    BRD = [list(input()) for _ in range(N)]
    min_cnt = 50 * 50
    B_first = [['B', 'W']*4]
    W_first = [['W', 'B']*4]

    for i in range(N - 8 + 1):
        for j in range(M - 8 + 1):
            W_cnt = 0  # 첫번째가 W로 시작하는 경우
            B_cnt = 0  # 첫번째가 B로 시작하는 경우
            for x in range(8):
                for y in range(8):
                    # 한줄씩 비교
                    # 짝수행 홀수행일때 시작값 다름
                    # 짝수행일때
                    if x % 2 == 0:
                        if BRD[i+x][j+y] != B_first[y]:
                            B_cnt += 1
                        if BRD[i + x][j + y] != W_first[y]:
                            W_cnt += 1
                    # 홀수행일때
                    else:
                        if BRD[i+x][j+y] != W_first[y]:
                            B_cnt += 1
                        if BRD[i+x][j+y] != B_first[y]:
                            W_cnt += 1

            min_cnt = min(min_cnt, W_cnt, B_cnt)
    print(min_cnt)
'''