# 4828 # 1일차 - min max

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    maxV, minV = lst[0], lst[0]
    for i in range(N):
        if maxV <= lst[i]:
            maxV = lst[i]
        if minV >= lst[i]:
            minV = lst[i]
    print(f'#{tc} {maxV - minV}')