import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H:
        floor, room = N % H, N // H + 1
    else:
        floor, room = H, N // H
    if len(str(room)) <= 1:
        print(f'{floor}0{room}')
    else:
        print(f'{floor}{room}')
