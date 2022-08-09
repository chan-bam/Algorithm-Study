# 백준 # 딱지놀이 # 14696

import sys
sys.stdin = open("bj14696in-딱지놀이.txt")

# 코드 줄이기

# count 함수 쓰면 for문 한개로도....

rounds = int(input())

for round in range(rounds): # 1, 2, 3, ...

    A_lst = list(map(int, input().split()))[1:]
    B_lst = list(map(int, input().split()))[1:]

    winner = 'D'

    for w in range(4, 0, -1):
        if A_lst.count(w) > B_lst.count(w):
            winner = 'A'
            break
        elif A_lst.count(w) < B_lst.count(w):
            winner = 'B'
            break

    print(winner)

'''

# 카운트배열 만들어서 개수 비교
# 첫번째 1개 날리는 것은 pop 불필요(슬라이싱으로 대체 가능)

rounds = int(input())

for round in range(rounds): # 1, 2, 3, ...

    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))

    A_len = A_lst.pop(0)
    B_len = B_lst.pop(0)

    # print(A_lst, B_lst)

    A_cnt = [0] * 5
    B_cnt = [0] * 5

    for a in A_lst:
        A_cnt[a] += 1

    for b in B_lst:
        B_cnt[b] += 1

    # print(A_count, B_count)

    winner = 'D'

    for w in range(4, 0, -1):
        if A_cnt[w] > B_cnt[w]:
            winner = 'A'
            break
        elif A_cnt[w] < B_cnt[w]:
            winner = 'B'
            break

    print(winner)

    # if A_cnt[4] > B_cnt[4]:
    #     winner = 'A'
    # elif A_cnt[4] < B_cnt[4]:
    #     winner = 'B'
    # elif A_cnt[3] > B_cnt[3]:
    #     winner = 'A'
    # elif A_cnt[3] < B_cnt[3]:
    #     winner = 'B'
    # elif A_cnt[2] > B_cnt[2]:
    #     winner = 'A'
    # elif A_cnt[1] < B_cnt[1]:
    #     winner = 'B'

'''