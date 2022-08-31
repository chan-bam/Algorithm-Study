import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

IOI = 'IO' * N + 'I'
length = 2 * N + 1
cnt = 0
i = 0
while i < M:
    if S[i] == IOI[0] and S[i:i + length] == IOI:
        cnt += 1
        i += length
        while True:
            if S[i:i + 2] == 'OI':
                cnt += 1
                i += 2
            else:
                i -= 2
                break
    i += 1
print(cnt)


'''
# 50점
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

IOI = 'IO' * N + 'I'

cnt = 0
i = 0
while i < M:
    if S[i] == IOI[0] and S[i:i + N * 2 + 1] == IOI:
        cnt += 1
    i += 1
print(cnt)
'''

'''
# 50점
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

IOI = 'IO' * N + 'I'

cnt = 0
i = 0
while i < M:
    if S[i] == IOI[0]:
        j = 1
        while j < 2 * N + 1 and i + j < M and S[i + j] == IOI[j]:
            j += 1
        if j == 2 * N + 1:
            cnt += 1
    i += 1
print(cnt)
'''