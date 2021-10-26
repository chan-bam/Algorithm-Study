import sys
sys.stdin = open("11586in.txt")

N = int(input()) # 마법거울의 크기를 나타내는 자연수

mirror = [list(input()) for _ in range(N)] # NxN크기의 거울

K = input() # 마법거울의 심리상태를 나타내는 정수 K

if K == '1': # 그대로 출력
    for i in mirror:
        print(''.join(i))

elif K == '2': # 좌우로 반전하여 출력
    for i in mirror:
        print(''.join(i[::-1]))

elif K == '3': # 상하로 반전하여 출력
    for i in range(N-1, -1, -1):
        print(''.join(mirror[i]))
