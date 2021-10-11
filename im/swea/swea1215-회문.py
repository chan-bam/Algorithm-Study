import sys
sys.stdin = open("1215in.txt")

def palindrome(arr):
    cnt = 0
    for i in range(8):
        for j in range(8-LEN+1):
            if arr[i][j:j+LEN] == arr[i][j:j+LEN][::-1]:
                cnt += 1
    return cnt

T = 10

for tc in range(1, T+1):
    LEN = int(input())

    arrW = [list(input()) for _ in range(8)]
    arrH = list(zip(*arrW))

    sumV = palindrome(arrW) + palindrome(arrH)

    print(f'#{tc} {sumV}')

