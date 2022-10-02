# 부분집합 # 비트마스킹 # 시간초과
N, M = map(int, input().split())

blackjack = list(map(int, input().split()))

lenBit = len(blackjack) # 원소의 개수
# print(N, M, blackjack, lenBit)
sumRes = []
### 부분집합 구하기 ###
for i in range(1 << lenBit): # 부분집합의 개수만큼 # 비트 비교
                            # 부분집합의 개수는 2**원소개수 # 1을 요소개수만큼 밀면 된다
    card = []

    cnt = 0
    sumV = 0
    for j in range(lenBit):
        if i & (1 << j):
            # print(blackjack[j], end=',')
            sumV += blackjack[j]
            cnt += 1
    # print()
    if cnt == 3:
        sumRes.append(sumV)

resV = 0

for r in sumRes:
    if resV < r <= M:
        resV = r

print(resV)