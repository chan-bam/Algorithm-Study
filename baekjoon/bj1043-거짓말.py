import sys
input = sys.stdin.readline

# union find
def union(a, b):
    a, b = find(a), find(b)
    if a in truth: # a가 진실을 알면
        parents[b] = a
    elif b in truth: # b가 진실을 알면
        parents[a] = b
    else:
        parents[a] = b

def find(x):
    while parents[x] != x:
        x = parents[x]
    return x
    # if parents[x] != x:
    #     parents[x] = find(parents[x])
    # return parents[x]

N, M = map(int, input().split()) # 사람의 수 N, 파티의 수 M
parents = list(range(N + 1))

T, *truth = map(int, input().split()) # 진실을 아는 사람의 수 + 번호
# M개의 줄 # 파티마다 오는 사람의 수와 번호
parties = []
for _ in range(M):
    P, *party = map(int, input().split())
    parties.append(party)
    for i in range(1, P):
        union(party[0], party[i])

cnt = 0
for p in parties:
    for i in p:
        if find(i) in truth:
            break
    else:
       cnt += 1
print(cnt)
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 사람의 수 N # 파티의 수 M

truth = set(map(int, input().split()[1:]))
party = [set(map(int, input().split()[1:])) for _ in range(M)]

for i in range(M):
    for attendee in party:
        if truth & attendee:   # truth.intersection(attendee) # set & set => 교집합 (&)
            truth |= attendee  # truth = truth.union(attendee) # 합집합한 결과값 저장 (|=) => 합집합 (|)

cnt = 0
for attendee in party:
    if truth - attendee == truth: # truth.difference(attendee) => 차집합(-)
        cnt += 1

print(cnt)

'''



'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 사람의 수 N # 파티의 수 M

truth = list(map(int, input().split()))  # 진실을 아는 사람의 번호
truth_num = truth.pop(0) # 진실을 아는 사람의 수     # == len(party)

party = [list(map(int, input().split())) for _ in range(M)] # 파티에 오는 사람의 수 + 파티에 오는 사람들의 번호

if not truth_num:
    print(len(party))
    exit(0)

temp = {}
union = set(truth)
while True:
    for j in party:
        for i in union:
            if i in j[1:]:
                union = set(list(union) + j[1:])
                break
    if union == temp:
        break
    temp = union

cnt = 0
for k in party:
    for z in union:
        if z in k[1:]:
            break
    else:
        cnt += 1

print(cnt)
'''

'''
6 5
1 6
2 4 5
2 1 2
2 2 3
2 3 4
2 5 6
answer: 0
'''