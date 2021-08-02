# # 프로그래머스 코딩테스트 문제
# def solution(price, money, count):
#     total = 0
    
#     for c in range(1, count+1):
#         moneyX = price * c
#         total += moneyX

#     if money < total:
#         return total - money

#     return 0

# print(solution(3, 20, 4))

# 윤년 고르기
# year = int(input())

# if year % 4 == 0 and year % 100 != 0:
#     print(1)
# elif year % 4 == 0 and year % 400 == 0:
#     print(1)
# else:
#     print(0)

# 사분면 고르기
# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# elif x > 0 and y < 0:
#     print(4)


# 알람시계
# h, m = map(int, input().split())

# if m - 45 < 0:
#     if h >= 1:
#         h -= 1
#         m = 60 + m - 45
#         print(h, m)
#     else:
#         h = 23
#         m = 60 + m - 45
#         print(h, m)
# else:
#     m = m - 45
#     print(h, m)

# 아주 간단한 계산기

# a, b = map(int, input().split())

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

