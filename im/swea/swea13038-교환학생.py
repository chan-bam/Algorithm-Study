import sys

# 왜 25개가 안맞는지 모를....

sys.stdin = open("13038in.txt")

T = int(input())

for tc in range(1, T+1):
    target = int(input())
    cross = list(map(int, input().split()))

    # 주당 수업일수
    days = cross.count(1)

    # 앞에 붙은 0의 개수 세기
    cntF = 0
    for i in range(len(cross)):
        if cross[i] == 1:
            break
        else:
            cntF += 1

    # 뒤에 붙은 0의 개수 세기
    cntB = 0
    for j in range(len(cross)-1, -1, -1):
        if cross[j] == 1:
            break
        else:
            cntB += 1

    # 안나누어 떨어지면 1주가 더 걸리는 것....
    divT = target % days
    if divT:
        tmpCnt = 0
        for k in range(len(cross)):
            if cross[k] == 1:
                tmpCnt += 1
                if tmpCnt == divT:
                    break
        result = target // days * 7 + k + 1 - cntF

    else:
        result = target // days * 7 - cntF - cntB

    print(f'#{tc} {result}')
