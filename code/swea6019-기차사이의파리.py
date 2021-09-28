import sys
sys.stdin = open("6019.txt")

T = int(input())

# Hint !
# 거리 = 속력 * 시간
# 시간 = 거리 / 속력

for tc in range(1, T+1):
    # D: 두 기차 전면부 사이의 거리 / A: 기차 A의 속력 / B: 기차 B의 속력 / F: 파리의 속력
    D, A, B, F = map(int, input().split())

    # res: 파리가 이동한 거리
    res = D / (A + B) * F
    # D / (A + B) == 기차 전면부 사이의 거리 / (기차A의 속력 + 기차B의 속력) = 기차 A, B가 서로를 향해 달려서 부딪치는데 걸리는 시간
    # ----------- * F ==  기차가 부딪치는데 걸리는 시간 * 파리의 속력 = 파리가 이동한 거리

    print(f'#{tc} {res}')