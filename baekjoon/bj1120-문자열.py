# 백준1220 # 문자열

A, B = input().split()

M = len(A) # 문자열 A의 길이
N = len(B) # 문자열 B의 길이

minDiff = M  # 가장 적게 차이나는 값을 저장할 변수를 초기화
            # 문자열 A의 길이 이상으로 차이가 날 수는 없으므로 A의 길이로 초기화
for i in range(N-M+1):  # 최대 (A의 길이 - B의 길이)번째 인덱스까지만 시작값으로 비교
    diff = 0  # 해당 구간에서 차이나는 값을 누적하여 저장할 변수
    for j in range(M): # 최대 (B의 길이-1)번째 인덱스 까지 비교
        if A[j] != B[i+j]: # j번째 인덱스 != j번째+0 -> j번째+1.. -> j번째+(B의길이-1)번째 까지 비교
            diff += 1  # 차이를 1 누적한다
    if diff < minDiff:   # 가장 적게 차이가 나는 최소값보다 새로 계산한 값이 더 적으면 
        minDiff = diff   # 최소값을 갱신한다
print(minDiff)   # 최종 저장된 최소값을 출력한다

# 문자열의 차이를 최소화하여 같아지도록 추가할 것이기 때문에...
# 기존의 문자열에서 제일 적게 차이나는대로 유지해서 추가하도록 되어있음
# 출력해야하는 것도 차이가 최소가 되도록 추가했을 때의 차이를 출력하도록 하기 때문에...
# 가장 적게 차이나는 구간을 찾아 그 차이를 반환하면 됨




'''
# 오답
cnt1 = 0
cnt2 = 0
tmp1 = B[:len(A)]
tmp2 = B[len(B) - len(A):]


for i in range(len(A)):
    if tmp1[i] != A[i]:
        cnt1 += 1
for j in range(len(A)):
    if tmp2[j] != A[j]:
        cnt2 += 1

if cnt1 < cnt2:
    print(cnt1)
else:
    print(cnt2)
'''

'''
while len(A) != len(B):
    cnt1 = 0
    cnt2 = 0
    tmp1 = B[:len(A)]
    tmp2 = B[len(B)-len(A):]

    for i in range(len(A)):
        if tmp1[i] == A[i]:
            cnt1 += 1
    for j in range(len(A)):
        if tmp2[j] == A[j]:
            cnt2 += 1

    if cnt1 > cnt2:
        A += B[len(A):len(A)+1]
    else:
        A = B[len(B)-len(A)-1:len(B)-len(A)] + A

print(A)
cnt = 0
for k in range(len(A)):
    if A[k] != B[k]:
        cnt += 1

print(cnt)
'''

# A_dic = {}
# B_dic = {}
#
# for a in A:
#     if a not in A_dic:
#         A_dic[a] = 1
#     else:
#         A_dic[a] += 1
#
# for b in B:
#     if b not in B_dic:
#         B_dic[b] = 1
#     else:
#         B_dic[b] += 1
#
# maxKey = 0
# keyDif = 0
# plusKey = ''
# for Bkey in B_dic:
#     keyDif = B_dic[Bkey] - A_dic[Bkey]
#     if keyDif >= maxKey:
#         maxKey = keyDif
#         plusKey = Bkey


# print(plusKey)
# print(A_dic, B_dic)
