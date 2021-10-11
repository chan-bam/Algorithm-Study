import sys
sys.stdin = open("11176in.txt")
T = int(input())

# print(ord('A'), chr(65))

# print(ord('I'), end=' ')
# print(ord('F'), end=' ')
# print(ord('C'))
# print(ord('H'), end=' ')
# print(ord('E'), end=' ')
# print(ord('B'))
# print(ord('G'), end=' ')
# print(ord('D'), end=' ')
# print(ord('A'))

for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    for i in range(N):
        for j in range(N*N+64, 64, -N):
            print(chr(j-i), end=' ')
        print()