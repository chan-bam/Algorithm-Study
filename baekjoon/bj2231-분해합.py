import sys
input = sys.stdin.readline
sys.stdin = open("2231in.txt")

N = int(input())

min_num = 1000000
for num in range(N-1, -1, -1):
    num_str = str(num)
    create = num
    for i in range(len(num_str)):
        create += int(num_str[i])
    # print('*', create)
    if create == N:
        if min_num > num:
            min_num = num
if min_num == 1000000: # 생성자가 없는 경우
    print(0) # 0을 출력
else: # 있는 경우
    print(min_num) # 최소값 출력