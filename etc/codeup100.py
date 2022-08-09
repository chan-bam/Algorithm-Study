# n = int(input())
# total = 0
# i = 1
# while total < n:
#     total += i
#     i += 1
# print(i-1)

# 16진수 구구단
# n = input()
# hexa = int(n, 16)
# # print(hexa)
# for i in range(1, 16):
#     print('%X'%hexa, '*%X'%i, '=%X'%(hexa*i), sep='')

# 369 박수
# n = int(input())
# for i in range(1, n + 1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')

# r, g, b = map(int, input().split())
# cnt = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
#             cnt += 1
# print(cnt)

# 소리계산
# h, b, c, s = map(float, input().split())
# print(round(h*b*c*s/8/1024/1024, 1), 'MB')

#이미지 계산
# w, h, b = map(int, input().split())
# res = float(w*h*b/8/1024/1024)
# print(format(res, '.2f'), 'MB')

#6086
# n = int(input())
# total = 0
# i = 1
# while True:
#     total += i
#     i += 1
#     if total >= n:
#         print(total)
#         break

#6087
# n = int(input())
# for i in range(1, n+1):
#     if i % 3 != 0:
#         print(i, end=' ')

#6088
# a, d, n = map(int, input().split())
# cnt = 1
#
# while cnt < n:
#     a += d
#     cnt += 1
# print(a)

#6089
# a, r, n = map(int, input().split())
# cnt = 1
#
# while cnt < n:
#     a *= r
#     cnt += 1
# print(a)

#6090

# a, m, d, n = map(int, input().split())
#
# cnt = 1
# while cnt < n:
#     a = a * m + d
#     cnt += 1
# print(a)

#6091
# a, b, c = map(int, input().split())
# d = 1
# while d % a != 0 or d % b != 0 or d % c != 0:
#     # 각각 0으로 나누어 떨어지는 날이 문제를 푸는 날임
#     # 세 날짜 모두 0 으로 나누어 떨어지는 날이 다 함께 문제를 푸는 날짜가 됨
#     d += 1
# print(d)

#6092
# n = int(input())
# lst = list(map(int, input().split()))
# cnt_lst = [0] * 24
# # print(cnt_lst)
# for i in lst:
#     cnt_lst[i] += 1
# # 1번부터 출력
# for j in range(1, len(cnt_lst)):
#     print(cnt_lst[j], end=' ')
#
# #print(' '.join(map(str, cnt_lst)))


#6093
# n = int(input())
# lst = list(map(int, input().split()))
# # for i in range(n-1, -1, -1):
# #     print(lst[i], end=' ')
# print(' '.join(map(str,lst[::-1])))

#6094
# n = int(input())
# # lst = list(map(int, input().split()))
# # print(min(lst))


#6095 바둑알 놓기 # 2차원 리스트
# n = int(input())
# BRD = [[0] * 20 for _ in range(20)]
# for i in range(n):
#     a, b = map(int, input().split())
#     BRD[a][b] = 1
# for i in range(1, 20):
#     for j in range(1, 20):
#         print(BRD[i][j], end=' ')
#     print()

#6096 바둑알 십자 뒤집기 #2차원 리스트
'''
BRD = [list(map(int, input().split())) for _ in range(1, 20)]
# 인덱스 1부터 시작하는 것에 주의
# print(BRD)
# 흰돌 1  # 검정돌 0

# 입력받을 좌표의 수
n = int(input())
for i in range(n):
    #가로, 세로 좌표
    x, y = map(int, input().split())
    # 10자 뒤집기
    # 해당 좌표 위치의 가로줄 돌의 색을 반대로 바꾸고, 세로줄 돌의 색을 반대로 바꾼다
    for j in range(1, 20):
        if BRD[x-1][j-1]:
            BRD[x-1][j-1] = 0
        else:
            BRD[x-1][j-1] = 1
    for k in range(1, 20):
        if BRD[k-1][y-1]:
            BRD[k-1][y-1] = 0
        else:
            BRD[k-1][y-1] = 1
for l in range(1, 20):
    for m in range(1, 20):
        print(BRD[l-1][m-1], end=' ')
    print()
'''

# 6987 설탕과자 뽑기 # 2차원리스트 뒤집는 문제
'''
h, w = map(int, input().split()) #격자판의 세로(행), 가로(열)
BRD = [[0] * w for _ in range(h)] # 열(가로로 쌓이는 열의 개수) # 행(세로로 쌓이는 줄의 개수)
# print(BRD)
n = int(input()) #막대의 개수
for i in range(n):
    l, d, x, y = map(int, input().split())
    #막대의 길이, 방향, 좌표(x,y)
    # print(h, w, n, l, d, x, y)
    # d: 가로는 0, 세로는 1
    if d == 0: # 가로인 경우
        for j in range(l):
            BRD[x-1][y+j-1] = 1
    else:
        for k in range(l):
            BRD[x+k-1][y-1] = 1
for i in range(h): #행
    for j in range(w): #열
        print(BRD[i][j], end=' ') #행우선 출력
    print()
'''

#6098 #성실한 개미
#개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직이고,
#오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다

# 오른쪽, 아래쪽이 2인 경우를 반드시 고려해야함!!!!
# 0, 2인 경우 == 1이 아닌 경우

MAZE = [list(map(int,(input().split()))) for _ in range(10)]
# print(MAZE)
i = 1 #행
j = 1 #열
while 0 < i < 9 and 0 < j < 9:

    if MAZE[i][j] == 2: # 2이면
        MAZE[i][j] = 9 # 2를 9로 바꾸고
        break # 종료

    if MAZE[i+1][j] == 1 and MAZE[i][j+1] == 1: # 아래쪽이 벽이고 오른쪽도 벽이면
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        break # 종료

    if MAZE[i][j+1] != 1: # 오른쪽이 길이거나 2이면
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        j += 1 #오른쪽으로 이동

    elif MAZE[i][j+1] == 1 and MAZE[i+1][j] != 1: # 오른쪽이 벽이고 아래쪽이 길이거나 2이면
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        i += 1 #아래로 이동


for i in range(10):
    for j in range(10):
        print(MAZE[i][j], end=' ')
    print()

'''
#블로그 코드 참조해서 풀었음

MAZE = [list(map(int,(input().split()))) for _ in range(10)]
# print(MAZE)
i = 1 #행
j = 1 #열
while True:
    if MAZE[i][j] == 2:
        MAZE[i][j] = 9 # 2를 9로 바꾸고
        break # 종료
    if MAZE[i+1][j] == 1 and MAZE[i][j+1] == 1: # 아래쪽이 벽이고 오른쪽도 벽이면
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        break # 종료
    if MAZE[i][j+1] != 1: # 오른쪽이 길이거나 "2"이면!!!
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        j += 1 #오른쪽으로 이동
    elif MAZE[i+1][j] != 1: # 아래쪽이 길이거나 "2"이면!!!
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        i += 1 #아래로 이동

for i in range(10):
    for j in range(10):
        print(MAZE[i][j], end=' ')
    print()
'''
'''
# 기존 시간초과 코드
# 오른쪽, 아래쪽이 2인 경우를 고려하지 않음

MAZE = [list(map(int,(input().split()))) for _ in range(10)]
# print(MAZE)
i = 1 #행
j = 1 #열
while 0 < i < 9 and 0 < j < 9:

    if MAZE[i][j+1] == 0: # 오른쪽이 길이면
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        j += 1 #오른쪽으로 이동

    elif MAZE[i][j+1] == 1 and MAZE[i+1][j] == 0: # 오른쪽이 벽이고 아래쪽이 길이면
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        i += 1 #아래로 이동

    elif MAZE[i+1][j] == 1 and MAZE[i][j+1] == 1: # 아래쪽이 벽이고 오른쪽도 벽이면
        MAZE[i][j] = 9     # 기존경로를 9로 바꿈
        break # 종료

    elif MAZE[i][j] == 2:
        MAZE[i][j] = 9 # 2를 9로 바꾸고
        break

for i in range(10):
    for j in range(10):
        print(MAZE[i][j], end=' ')
    print()
'''