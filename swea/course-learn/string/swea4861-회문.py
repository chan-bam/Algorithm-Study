import sys

sys.stdin = open("4861in.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # N x N 글자판의 길이   # M: 찾아야하는 회문의 길이
    N, M = map(int, input().split())
    BRD = [input() for _ in range(N)]
          # --------- input()으로 하면 그냥 한줄 문자열로 입력받게됨
          # list함수 씌우면 입력받은 하나의 문자열 문자별 한개별로 각각 나눠서 리스트에 입력됨
    # print(BRD)

    res = ''
    # 가로 회문 판별
    for i in range(N):
        for j in range(N-M+1):
            tmp = BRD[i][j:j+M]
        if tmp == tmp[::-1]:
            res = tmp
            break

    # 세로 회문 판별
    if res == '': # 가로 회문 아니면
        for k in range(N):
            for x in range(N-M+1):
                tmp2 = ''      # 초기화의 위치가 중요...!!
                for m in range(M):
                    tmp2 += BRD[m+x][k]
                if tmp2 == tmp2[::-1]:
                    res = tmp2
                    break

    print(f'#{tc} {res}')


