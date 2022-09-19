expression = input()
stack, result = [], ''

for x in expression:
    if x.isalpha(): # == 65 <= ord(x) <= 90 # 피연산자이면
        result += x
    elif x == '(':
        stack.append(x)
    elif x in '*/':
        while stack and stack[-1] in '*/': # 스택에 있는 *, / 연산자를 만나기 전까지
            result += stack.pop()
        stack.append(x) # 연산자를 스택에 추가
    elif x in '+-':
        while stack and stack[-1] != '(': # 스택에 있는 ( 연산자를 만나기 전까지
            result += stack.pop()
        stack.append(x) # 연산자를 스택에 추가
    elif x == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop() # 스택에서 '('을 제거
while stack: # 스택에 남아 있는 연산자
    result += stack.pop()

print(result)

'''
import sys

expression = sys.stdin.readline().rstrip()
stack = []
result = ''

for x in expression:
    if x.isalpha(): # 피연산자
        result += x
    # 연산자
    elif x == '(':
        stack.append(x)
    elif x in '*/':
        while stack and stack[-1] in '*/':
            result += stack.pop()
        stack.append(x)
    elif x in '+-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()

# stack안에 남아있는 값 pop
while stack:
    result += stack.pop()

print(result)

'''