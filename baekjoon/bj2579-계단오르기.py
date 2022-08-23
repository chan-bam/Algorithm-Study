import sys
input = sys.stdin.readline

N = int(input().rstrip())
stairs = [0] + [int(input().rstrip()) for _ in range(N)] + [0]
                                                        # N이 1인 경우 index error 방지
                                                        # (N은 300이하의 자연수)
score = [0] * (N + 2)

score[1], score[2] = stairs[1], stairs[1] + stairs[2]

for i in range(3, N + 1):
    score[i] = max(score[i - 3] + stairs[i - 1], score[i - 2]) + stairs[i]

print(score[N])