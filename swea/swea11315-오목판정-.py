import sys
sys.stdin = open("11315in.txt")

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    # print(arr)

    # 가로, 세로인 경우
    ans = 0
    for i in range(n):
        for j in range(n - 4):
            cnt = 0
            for k in range(5):
                if arr[i][j + k] == 'o':
                    cnt += 1
            if cnt == 5:
                ans += 1

            cnt = 0
            for h in range(5):
                if arr[j + h][i] == 'o':
                    cnt += 1
            if cnt == 5:
                ans += 1

    # 대각선인 경우
    for k in range(n - 4):
        for m in range(n - 4):
            cnt = 0
            for z in range(5):
                if arr[k + z][m + z] == 'o':
                    cnt += 1
            if cnt == 5:
                ans += 1
            cnt = 0
            for z in range(5):
                if arr[k + z][m + 4 - z] == 'o':
                    cnt += 1
            if cnt == 5:
                ans += 1

    print('#{}'.format(tc), end=' ')
    if ans > 0:
        print('YES')
    else:
        print('NO')