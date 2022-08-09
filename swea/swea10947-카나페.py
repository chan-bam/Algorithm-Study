import sys
sys.stdin = open("10947in.txt")

T = int(input())

for tc in range(1, T + 1):
    # 비스킷과 재료들의 맛 N개 # 카나페들의 맛의 합의 최댓값 구하기
    N = int(input())
    biscuit = sorted(list(map(int, input().split())))  # 큰값끼리 곱할 수록 합이 최대가 되므로... # 내림차순 정렬
    ingredient = sorted(list(map(int, input().split()))) # 내림차순 정렬

    result = 0
    for i in range(N):
        result += (biscuit[i] * ingredient[i])

    print(f'#{tc} {result}')
