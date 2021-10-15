T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                lst.append([i, j])
    print(lst)
    nemo = []
    for s in lst:
        x = s[0]
        y = s[1]
        w = h = 1
        while y < N and arr[x][y + 1] == 1:
            y += 1
            w += 1
            if arr[x][y + 1] != 1:
                break

        while x < N and arr[x + 1][y] == 1:
            x += 1
            h += 1
            if arr[x + 1][y] != 1:
                break

        nemo.append(w * h)
    print(nemo)
    print('#{} {}'.format(tc, max(nemo)))
'''
arr = [
    [1, 2],
    [0, 2],
    [1, 3],
    [2, 3]
]
# 람다를 사용하여 2차원배열 우선순위 정하여 정렬할 수 있다고....
# 딕셔너리의 경우는 넓이를 키로 밸류값 가로세로 저장해놓고 밸류값 정렬하는건가....?? 이건 모르겠다
arr.sort(key = lambda x:(x[0]*x[1], x[1]), reverse=True) # 역순도 가능
print(arr)
'''

'''
import sys
sys.stdin = open("../../../SSAFY/code/12726in.txt")

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for k in range(1, M+1): # k의 영역은 1부터 M까지
        for i in range(N):
            for j in range(N):
                if M % k == 0: # 전체토글
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1
                elif (i + j +2) % k == 0:
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1
    if k == M:
        for x in range(N):
            for y in range(N):
                if arr[x][y] == 1:
                    cnt += 1

    print(f'#{tc} {cnt}')
'''