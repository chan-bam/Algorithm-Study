'''
N = int(input())
for i in range(1, 10):
    print(N, '*', i, '=', N*i)
'''

'''
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(a + b)
'''
'''
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)
'''
'''
import sys
N = int(input())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
'''
'''
N = int(input())
for i in range(1, N+1):
    print(i)
'''
'''
N = int(input())
for i in range(N, 0, -1):
    print(i)
'''
'''
N = int(input())

for tc in range(1, N+1):
    A, B = map(int, input().split())
    print('Case #{}: {}'.format(tc, A+B))
'''
'''
N = int(input())

for tc in range(1, N+1):
    A, B = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(tc, A, B, A+B))
'''
'''
N = int(input())

for i in range(1, N + 1):
    print('*' * i)
'''

'''
# 블로그 참조해서 풀이
N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i), '*'*i, sep='')
'''
'''
N, X = map(int, input().split())
lst = list(map(int, input().split()))
for i in lst:
    if i < X:
        print(i, end=' ')
print()
'''
'''
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)
'''
'''
# 블로그 참조해서 풀이
# EOF 처리
try:
    while True:
        a, b = map(int, input().split())
        print(a+b)
except:
    print('')
'''
'''
#다시풀기
N = input()
cnt = 1
B = str(int(N[1])) + str(int(N[0]) + int(N[1]))[-1] # 문자열 슬라이싱
# print(B)
while B != N:
    B = str(int(B[1])) + str(int(B[0]) + int(B[1]))[-1] #문자열 슬라이싱
    # print(B)
    cnt += 1
print(cnt)
'''

#미완_더하기 사이클
'''
N = input()
B = N
C = int(N)
cnt = 1
total = 0
while C % 10 != 0:
    total += (C % 10)
    C = C // 10
while B[-1]+str(total)[-1] != N:
'''

'''
N = int(input())
lst = list(map(int, input().split()))
maxV = lst[0]
minV = lst[0]
for i in lst:
    if maxV < i:
        maxV = i
    if minV > i:
        minV = i
print(minV, maxV)

lst = []
for i in range(9):
    lst += [int(input())]
maxV = lst[0]
for i in range(9):
    if lst[i] >= maxV:
        maxV = lst[i]
        maxP = i
print(maxV)
print(maxP+1)

# 카운트 배열
A = int(input())
B = int(input())
C = int(input())

ABC = str(A * B * C)

cntLst = [0] * 10

for i in ABC:
    cntLst[int(i)] += 1
for j in cntLst:
    print(j)

cntLst = [0] * 42
for i in range(10):
    cntLst[int(input()) % 42] += 1

cnt = 0
for j in cntLst:
    if j != 0:
        cnt += 1
print(cnt)

LST = []
N = int(input())

LST = list(map(int, input().split()))
maxV = LST[0]
for i in LST:
    if maxV < i:
        maxV = i
# print(LST)
# print(maxV)
sumV = 0
for j in LST:
    sumV += (j/maxV*100)
# print(sumV)
print(round(sumV/len(LST),6))



# 8958 OX퀴즈 문제... gg
N = int(input())

for i in range(N):
    OX = list(input())

    sumV = 0  # 점수 누적할 변수
    score = 0  # 누적할 점수 변수 초기화

    for i in OX:
        if i == 'O':  # i가 'O'이면
            score += 1  # 점수를 1 증가시킨다(연속해서 나오면 1 증가된 값을 누적하도록)
            sumV += score  # sumV에 점수를 누적한다
        else:  # i가 'O' 아니면, 'X'이면
            score = 0  # 누적할 점수 초기화  # 이후 'O'이 나오면 다시 1부터 누적해야 하므로
    print(sumV)



# 4344
C = int(input())

for tc in range(C):
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    sumV = 0
    for i in lst:
        sumV += i
    avgV = sumV // N
    cnt = 0
    for i in lst:
        if i > avgV:
            cnt += 1
    print(f'{round(cnt/N*100, 3):.3f}','%', sep='') # 소수점 자리수 출력하는 법!!!!


N = input()
cnt = 1
if len(N) == 1:
    N += '0'
    B = str(int(N[1])) + str(int(N[0]) + int(N[1]))[-1] # 문자열 슬라이싱
else:
    B = str(int(N[1])) + str(int(N[0]) + int(N[1]))[-1]  # 문자열 슬라이싱

while B != N:
    B = str(int(B[1])) + str(int(B[0]) + int(B[1]))[-1] #문자열 슬라이싱
    cnt += 1
print(cnt)


#11654 아스키코드
print(ord(input()))


#11720 숫자의 합
N = int(input())
wrd = input()
sumV = 0
for i in range(N):
    sumV += int(wrd[i])

print(sumV)


# 10809 알파벳 찾기
wrd = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    for j in range(len(wrd)):
        if wrd[j] == i:
            print(j, end=' ')
            break
    else: # for~else 구문 : for문 안에 해당되는 케이스 없으면 else구문 실행
        print(-1, end=' ')




#2675 문자열 반복
T = int(input())
for tc in range(T):
    R, S = input().split()
    R = int(R)
    for i in S:
        print(i * R, end='')
    print()

'''
'''
#1157 단어 공부

# print(wrd)
# wrd_cnt = [0]*(122-64)

# print(ord('A')-ord('a')) # -32
# print(ord(''))
# print(ord('Z')-ord('A')+1) # 26개

# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))

# ord함수와 카운트배열 사용 ---실패

wrd = input().upper() # 대문자 기준으로 반환해야하므로 문자열을 전부 대문자로 변환

cnt_dic = {} # 문자별로 cnt 셀 딕셔너리 생성
for i in range(len(wrd)): # 문자별로 반복
    if wrd[i] not in cnt_dic: # cnt_dic에 없으면
        cnt_dic[wrd[i]] = wrd.count(wrd[i]) # 갯수를 세서 입력한다

maxV = cnt_dic[wrd[0]]

for key, val in cnt_dic.items(): # 가장 큰 값과 key를 가져온다
    if val >= maxV:
        maxV = val
        maxKey = key

cnt = 0
for j in cnt_dic.values(): # max값이 두개 이상이면
    if j == maxV:
        cnt += 1 # cnt를 늘린다

if cnt > 1: # cnt가 1 이상이면
    print('?') # 가장 많은 문자가 두개 이상이면 '?'출력
else: # 1개 이하이면
    print(maxKey) # 가장 많은 문자 출력

'''

# 1152번 단어의 개수
# sentence = input()
# senLst = list(map(str, sentence.split()))
# print(len(senLst))

# 한줄로1
# print(len(list(map(str, input().split()))))

# 한줄로2
# print(len(input().split()))

# 자동으로 리스트로 생성됨
# print(input().split())


# 2908번 상수 문제
# A, B = input().split()
# newA = int(A[2]+A[1]+A[0])
# newB = int(B[2]+B[1]+B[0])
# if newA > newB:
#     print(newA)
# else:
#     print(newB)


'''
# 문자열 뒤집기
A = '123'
A = int(A[::-1])
print(A)
'''
'''
# 2908번 상수 문제 # 문자열 뒤집기로 풀기!
A, B = input().split()
newA = int(A[::-1])
newB = int(B[::-1])
if newA > newB:
    print(newA)
else:
    print(newB)
'''


'''
# 5622 # 다이얼

# 다이얼별로 걸리는 시간:다이얼알파벳을 key, value로 매핑
# value값에 포함이 되어있으면 key값을 더해주는 방식
DIAL = {2: '1',
        3: 'ABC', 4: 'DEF', 5: 'GHI', 6: 'JKL',
        7: 'MNO', 8: 'PQRS', 9: 'TUV', 10: 'WXYZ',
        11: '0'}
wrd = input()
time = 0
for w in wrd:
    for d in DIAL:
        if w in DIAL[d]: # value값 안에 포함이 되어있으면
            time += d # key값을 더함
print(time)
'''

# 손익분기점
A, B = map(int, input().split())

print(A + B)