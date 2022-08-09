
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    PASCAL = [[0]*(N) for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if j == 0:
                PASCAL[i][j] = 1
            elif j == i:
                PASCAL[i][j] = 1
            else:
                PASCAL[i][j] = PASCAL[i-1][j-1] + PASCAL[i-1][j]

    print(f'#{tc}')
    for k in range(N):
        for m in range(N):
            if PASCAL[k][m] != 0:
                print(PASCAL[k][m], end =' ')
        print()
    # print(PASCAL)
'''
# 예전 코드
T = int(input())

# print(T)
for tc in range(1, T+1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]

    for i in range(N):
        lst[i][0] = 1
        lst[i][i] = 1

    for i in range(2, N):
        for j in range(1, i):
            if lst[i][j] == 0:
                lst[i][j] = lst[i - 1][j - 1] + lst[i - 1][j]

    print('#{}'.format(tc))
    for i in lst:
        for j in i:
            if j != 0:
                print(j, end=' ')
        print()

'''