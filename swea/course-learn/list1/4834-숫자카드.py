import sys
sys.stdin = open("4834in.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 카드의 장수: N
    numCard = input()
    cntDic = {}

    for card in numCard:
        if int(card) in cntDic:
            cntDic[int(card)] += 1
        else:
            cntDic[int(card)] = 1

    maxV = 0
    maxKey = 0

    for key, val in cntDic.items():
        if maxV <= val:
            maxV = val
            if maxKey <= key:
                maxKey = key

    print(f'#{tc} {maxKey} {maxV}')
