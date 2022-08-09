
N, M = map(int, input().split())

blackjack = list(map(int, input().split()))

res_set = set()
for a in blackjack:
    for b in blackjack:
        for c in blackjack:
            if a != b and a != c and b != c:
                res_set.add(a+b+c)

resV = 0

if M in res_set: # 합계중에 M과 같은 수가 있으면 M이 가장 큰값이므로 M을 출력
    print(M)
else:
    for r in res_set: # 정렬해서 큰값부터 비교하는게 빠를수도....?
        if resV < r <= M:
            resV = r
    print(resV)


'''
N, M = map(int, input().split())

blackjack = list(map(int, input().split()))

res_set = set()
for a in blackjack:
    for b in blackjack:
        for c in blackjack:
            if a != b and a != c and b != c:
                res_set.add(a+b+c)

resV = 0

if M in res_set: # 합계중에 M과 같은 수가 있으면 M이 가장 큰값이므로 M을 출력
    print(M)
else:
    for r in res_set: # 정렬해서 큰값부터 비교하는게 빠를수도....?
        if resV < r <= M:
            resV = r
    print(resV)
'''