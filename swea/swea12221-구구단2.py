import sys
sys.stdin = open("12222in.txt")

T = int(input())

gugu = set()

for i in range(1, 10):
    for j in range(1, 10):
        gugu.add(i*j)

for tc in range(1, T+1):
    N = int(input())
    if N in gugu:
        result = "Yes"
    else:
        result = "No"
    print(f'#{tc} {result}')