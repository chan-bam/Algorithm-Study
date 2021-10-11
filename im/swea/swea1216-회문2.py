import sys
sys.stdin = open("1216in.txt")

# 앞에서부터 전부 찾아서 최대값을 찾는다 --> 오래걸림!!!
def palindrome(arr):
    maxV = 1
    for n in range(N):
        for i in range(N):
            for j in range(N - n + 1):
                judge = arr[i][j:j+n]
                if len(judge) > maxV:
                    if judge == judge[::-1]:
                        maxV = len(judge)
                        print(maxV)
    return maxV

# 큰 길이부터 찾으면... 가장 긴 회문 나오면 리턴
def palindrome_back(arr):
    for n in range(N-1, 0, -1):
        for i in range(N):
            for j in range(N - n + 1):
                judge = arr[i][j:j+n]
                if judge == judge[::-1]:
                    return len(judge)

# 100X100 평면
T = 10
N = 100

for t in range(1, T+1):
    tc = int(input())
    arrW = [list(input()) for _ in range(N)]
    arrH = list(zip(*arrW))
    # arrW_pal = palindrome(arrW)
    # arrH_pal = palindrome(arrH)
    arrW_pal = palindrome_back(arrW)
    arrH_pal = palindrome_back(arrH)
    if arrW_pal >= arrH_pal:
        result = arrW_pal
    else:
        result = arrH_pal

    print(f'#{tc} {result}')