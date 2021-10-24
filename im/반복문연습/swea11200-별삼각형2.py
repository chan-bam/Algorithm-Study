import sys

sys.stdin = open("11200in.txt")

# 삼각형의 높이 N과 종류 M (N, M은 홀수)

'''
#1
*
**
***
**
*
#2
  *
 **
***
 **
  *
#3
*****
 ***
  *
 ***
*****
#4
***
 **
  *
  **
  ***
'''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{tc}')
    # 삼각형 1
    if M == 1:
        for i in range(N): # 높이 N까지 별을 출력
            if i <= N//2:
                print('*' * (i + 1))
            else:
                print('*' * (N - i))

    # 삼각형 2
    if M == 2:
        for i in range(N): # 높이 N까지 별을 출력
            if i <= N//2:
                print(' '*(N//2-i) + '*'*(i+1))
            else:
                print(' '*(i-N//2) + '*'*(N-i))

    # 삼각형 3
    if M == 3:
        for i in range(N): # 높이 N까지 별을 출력
            if i <= N//2:
                print(' '*i + '*'*(N-i*2))
            else:
                print(' '*(N-i-1) + '*'*(N-(N-i-1)*2))

    # 삼각형 4
    if M == 4:
        for i in range(N): # 높이 N까지 별을 출력
            if i <= N//2:
                print(' '*i + '*'*(N//2-i+1))
            else:
                print(' '*(N//2) + '*'*(i-1))