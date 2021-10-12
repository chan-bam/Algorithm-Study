import sys
sys.stdin = open("5432in.txt")

T = int(input())

for tc in range(1, T+1):
    pipes = list(input())

    # print(pipes)
    sumV = 0
    stk = [] # 스택 사용

    for i in range(len(pipes)): # 인덱스로 비교한다 # 이전것을
        if pipes[i] == '(':
            stk.append(pipes[i]) # 스택에 입력한다... 괄호검사는 뭔가 스택이 잘어울린다(?) # 하지만 스택에 있는 요소가 크게 중요한 역할을 하는 것은 아니라... 문자열문제에 가깝다..!
        else:    # ')' 이면
            if pipes[i-1] == '(':   # 이전것이 열린괄호이면 - > 레이저
                stk.pop()  # 스택에 있는 것을 빼고
                sumV += len(stk)    # 스택의 길이를 누적 # 스택에 남은 것들 : 이어지고 있는 쇠막대 == 잘린 쇠막대기의 개수
            if pipes[i-1] == ')':    # 이전것이 닫힌 괄호이면 - > 쇠막대기의 끝이다
                stk.pop()   # 스택에 있는 것을 하나 빼고 (이어지고 있지 않으므로)
                sumV += 1   # 잘린 쇠막대기의 개수를 하나 누적한다 -> 한조각이 떨어져나오므로....

    print(f'#{tc} {sumV}')