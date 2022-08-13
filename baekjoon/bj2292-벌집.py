import sys
input = sys.stdin.readline

N = int(input())

# [[1], [2, 3, 4, 5, 6, 7 : 6개], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 : 12개], [20, ... 37 : 18개]]
#                          6*1개                                                 6*2개                 6*3개
#   1      2 ~ 7                      8 ~ 19                                                20 ~ 37
#              1+6                      7+6*2                                                  19+6*3
#   1      2                           3                                                      4

bee_house = 1
cnt = 1

while N > bee_house:
    bee_house += cnt * 6
    cnt += 1

print(cnt)
