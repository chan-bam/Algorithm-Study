N = int(input())

for _ in range(N):
    PS = input()
    stk = []
    for p in PS:
        if p == '(':
            stk.append(p)
        elif p == ')':
            if len(stk):
                stk.pop()
            else:
                print('NO')
                break
    else:
        if len(stk):
            print('NO')
        else:
            print('YES')

