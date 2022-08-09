import sys
sys.stdin = open("4836in.txt")

# 테스트 케이스의 개수 : T
T = int(input())

for tc in range(1, T+1):

    # 칠할 영역의 개수 : N
    N = int(input())

    # 10X10 격자

    BRD = [[0] * 10 for _ in range(10)]
    # print(BRD)
    for i in range(N):
        # 왼쪽 위 모서리 인덱스 r1, c1 # 오른쪽 아래 모서리 인덱스 r2, c2 # color: 1은 빨강, 2는 파랑
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(r1, r2+1): # r1에서 r2까지
            for k in range(c1, c2+1): # c1에서 c2까지
                BRD[j][k] += color (빨간색:1일때 1을 더함 파란색:2일때 2를 더함)

    # 보라색이 된 칸(3이 된 칸) 수를 구하기
    cnt = 0
    for i in range(10):
        for j in range(10):
            if BRD[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')

