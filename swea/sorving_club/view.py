import sys
sys.stdin = open("view.txt")

for tc in range(1, 11):
    N = int(input())
    BUILD = list(map(int, input().split()))
    sumV = 0
    for i in range(2, N-2):
        maxV = max(BUILD[i-2], BUILD[i-1], BUILD[i+1], BUILD[i+2])
        if maxV < BUILD[i]:
            sumV += (BUILD[i] - maxV)
    print(f'#{tc} {sumV}')
