import sys
sys.stdin = open("11159in.txt")

T = int(input())

for tc in range(1, T+1):
    # 너비 W : 높이 H
    H, W = map(int, input().split())

    print(f'#{tc}')
    for i in range(1, H * W + 1):
        print(i, end = ' ')
        if i == H * W:
            break
        elif i % (H + 1) == 0:
            print()
    print()

'''

# 참조 코드1
TC = int(input())
for test_case in range(1, TC+1):
    H, W = map(int,input().split())
    temp = 0
    print('#{}'.format(test_case))
    for i in range(1, H+1):
        for j in range(1, W+1):
            j += temp
            print(j, end=' ')
        temp += W
        print()
        
# 참조 코드2
TC = int(input())
for test_case in range(1, TC+1):
    H, W = map(int,input().split())
    print('#{}'.format(test_case))
    for i in range(1, H+1):
        for j in range(1, W+1):
            j += W*(i-1)
            print(j, end=' ')
        print()

'''