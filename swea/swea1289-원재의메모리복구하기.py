import sys
sys.stdin = open("1289in.txt")

# int로 받으면 int로 str으로 받으면 str로 비교 ---> 단순한 문제지만 실수하면 당황할 수 있으므로 주의!!!!!!
# 따옴표 찍기 번거로우니...? 숫자가 결과값에 영향 주는거 아니면 웬만하면 int로 받자

T = int(input())
for tc in range(1, T+1):
    target = list(map(int, input()))
    N = len(target)
    memory = [0] * N
    cnt = 0
    for i in range(N):
        if target[i] != memory[i]:
            cnt += 1
            for j in range(i, N):
                if target[i] == 1:
                    memory[j] = 1
                else:
                    memory[j] = 0
            if memory == target:
                break
    print(f'#{tc} {cnt}')


'''
T = int(input())
for tc in range(1, T+1):
    target = list(input())
    N = len(target)
    memory = ['0'] * N
    cnt = 0
    for i in range(N):
        if target[i] != memory[i]:
            cnt += 1
            for j in range(i, N):
                if target[i] == '1':
                    memory[j] = '1'
                else:
                    memory[j] = '0'
            if memory == target:
                break
    print(f'#{tc} {cnt}')
'''

