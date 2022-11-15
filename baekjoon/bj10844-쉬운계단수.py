import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N - 1]) % 1_000_000_000)

# import sys
# input = sys.stdin.readline
#
# N = int(input()) # 길이가 N인 계단수
#
# dp = [[0] * 10 for j in range(N)]
# for i in range(1, 10): # 맨 앞자리가 0일 때는 횟수를 세지 않는다.
#     dp[0][i] = 1
#
# for i in range(1, N):
#     for j in range(10):
#         if j == 0: # 0일때는 뒤에 1밖에 올 수 없다
#             dp[i][j] = dp[i - 1][1]
#         elif j == 9: # 9일때는 뒤에 8밖에 올 수 없다
#             dp[i][j] = dp[i - 1][8]
#         else: # 1 ~ 8일때는 -1 +1인 숫자가 올 수 있다.
#             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
#
# print(sum(dp[N - 1]) % 1_000_000_000)



# N == 1 => 1, 2, 3, 4, 5, 6, 7, 8, 9 # vacant truth 에 의하여 그러지 않아야 할것 같지만 그냥 예외 처리
# N == 2 => 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98 # 17개
# N == 3 => 101,
#           121, 123
#           212, 210
#           232, 234
#           321, 323
#           343, 345
#           432, 434
#           454, 456
#           543, 545
#           565, 567
#           654, 656
#           676, 678
#           765, 767
#           787, 789
#           876, 878
#           989, 987
#           898

# 0을 제외한 모든 숫자는 앞에 올 수 있다
# 1~8은 뒤에 올 수 있는 숫자가 총 2종류(숫자±1)
# 9 뒤엔 숫자 8만 올 수 있다
# dp테이블은 이차원 리스트이며 dp[자리 수][앞에 오는 숫자]=경우의 수

