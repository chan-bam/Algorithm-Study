import sys
sys.stdin = open("12726in.txt")

# toggle
# im은 pass했지만 XOR연산 방식 1->0 0->1 전환 생각나서 다시 풀어봄

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    ONF = [list(map(int, input().split())) for _ in range(N)]

    for m in range(1, M + 1):
        for k in range(N):
            for u in range(N):
                if m == M or M % m == 0 or (k + u + 2) % m == 0:
                    ONF[k][u] ^= 1

    lights = 0
    for on in ONF:
        lights += on.count(1)
    print(f'#{tc} {lights}')
