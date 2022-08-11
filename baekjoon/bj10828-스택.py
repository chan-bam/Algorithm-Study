import sys
input = sys.stdin.readline

N = int(input())

stk = []
for _ in range(N):
    operation = input().rstrip()
    if operation == 'pop': # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(stk):
            print(stk.pop())
        else:
            print('-1')
    elif operation == 'size': # 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stk))
    elif operation == 'empty': # 스택이 비어있으면 1, 아니면 0을 출력한다.
        if len(stk):
            print('0')
        else:
            print('1')
    elif operation == 'top': # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(stk):
            print(stk[-1])
        else:
            print('-1')
    else: # 정수X를 스택에 넣는 연산(push X)
        stk.append(operation.split()[-1])



