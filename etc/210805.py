# 대각선 출력하기

# i = 0
# while i < 5:
#     j = 0
#     while j < 5:
#         if i == j:
#             print("#", end='')
#         else:
#             print("+", end='')
#         j += 1
#     print()
#     i += 1

# 간단한 N의 약수
# N = int(input())

# for n in range(1, N+1):
#     if N % n == 0:
#         print(n, end = ' ')

# 더블더블
# N = int(input())
# num = 1
# print(1, end = ' ')
# for n in range(1, N + 1):
#     num *= 2
#     print(num, end = ' ')

# 거꾸로 출력해보아요
N = int(input())

while N >= 0:
    print(N, end = ' ')
    N -= 1