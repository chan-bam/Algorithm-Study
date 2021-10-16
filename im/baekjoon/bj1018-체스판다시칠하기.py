import sys
input = sys.stdin.readline

N, M = map(int, input().split())
BRD = [list(input()) for _ in range(N)]
min_cnt = 50 * 50
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        W_cnt = 0  # 첫번째가 W로 시작하는 경우
        B_cnt = 0  # 첫번째가 B로 시작하는 경우
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0 and BRD[i + x][j + y] == 'B':  # 합이 짝수인 좌표 (첫번째칸)
                    W_cnt += 1
                if (x + y) % 2 == 1 and BRD[i + x][j + y] == 'W':  # 합이 홀수인 좌표 (두번째칸)
                    W_cnt += 1
                if (x + y) % 2 == 0 and BRD[i + x][j + y] == 'W':  # 합이 짝수인 좌표 (첫번째칸)
                    B_cnt += 1
                if (x + y) % 2 == 1 and BRD[i + x][j + y] == 'B':  # 합이 홀수인 좌표 (두번째칸)
                    B_cnt += 1
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
    min_cnt = 50*50
    for i in range(N-8+1):
        for j in range(M-8+1):
            W_cnt = 0 # 첫번째가 W로 시작하는 경우
            B_cnt = 0 # 첫번째가 B로 시작하는 경우
            for x in range(8):
                for y in range(8):
                    if (x+y) % 2 == 0 and BRD[i+x][j+y] == 'B': # 합이 짝수인 좌표 (첫번째칸)
                        W_cnt += 1
                    if (x+y) % 2 == 1 and BRD[i+x][j+y] == 'W': # 합이 홀수인 좌표 (두번째칸)
                        W_cnt += 1
                    if (x+y) % 2 == 0 and BRD[i+x][j+y] == 'W': # 합이 짝수인 좌표 (첫번째칸)
                        B_cnt += 1
                    if (x+y) % 2 == 1 and BRD[i+x][j+y] == 'B': # 합이 홀수인 좌표 (두번째칸)
                        B_cnt += 1
            min_cnt = min(min_cnt, W_cnt, B_cnt)
    print(min_cnt)
'''