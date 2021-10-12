import sys
sys.stdin = open("5432in.txt")

T = int(input())

for tc in range(1, T+1):
    pipes = list(input())

    # print(pipes)
    sumV = 0 # 잘린 파이프의 조각의 개수를 저장할 변수
    pipe_or_lazerStart = 0 # 이어지고있는 파이프의 개수를 저장할 변수

    for i in range(len(pipes)):
        if pipes[i] == '(':
            pipe_or_lazerStart += 1
        else:
            if pipes[i-1] == '(': # 레이저
                pipe_or_lazerStart -= 1 # 레이저시작으로 인해 들어간 개수는 빼주고
                sumV += pipe_or_lazerStart # 이어지고있는 쇠막대기의 조각을 합계로 누적한다
            else: # 쇠막대기의 끝
                pipe_or_lazerStart -= 1 # 이어지고 있는 쇠막대기의 개수를 빼준다
                sumV += 1 # 잘려나간 조각의 개수를 입력한다
    print(f'#{tc} {sumV}')

