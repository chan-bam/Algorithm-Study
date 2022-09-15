T = int(input())

for _ in range(T):
    a, b = map(int, input().split()) # a : 1 ~ 99 / b : 1 ~ 999,999
    a %= 10
    if not a:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        b %= 2
        if b: # 1이면
            print(a)
        else: # 2이면
            print(a ** 2 % 10)
    else: # 2, 3, 7, 8
        b %= 4
        if b: # 1 ~ 3이면
            print(a ** b % 10)
        else: # 4이면
            print(a ** 4 % 10)

'''
# 1 => 1
# 2 => 2 4 8 6
# 3 => 3 9 7 1
# 4 => 4 6
# 5 => 5
# 6 => 6
# 7 => 7 9 3 1
# 8 => 8 4 2 6
# 9 => 9 1
'''
