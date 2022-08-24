import sys
sys.stdin = open("1234in.txt")

for tc in range(1, 11):
    N, PW = input().split()
    stk = []
    for i in range(int(N)):
        if stk and PW[i] == stk[-1]:
            stk.pop()
        else:
            stk.append(PW[i])
    password = ''.join(stk)
    print(f'#{tc} {password}')