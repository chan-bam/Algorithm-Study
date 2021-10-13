import sys
sys.stdin = open("1979in.txt")

# 연속된 1의 개수가 k인 경우  # 1차원배열에서 연속한 1의 개수를 셀 수 있는가
# 찾는 방법 # 연속한 1의 최대 개수를 찾는 문제

# 연속한 1의 개수 중 최대값 # 중간에 0이 나오면 reset시켜야함....... # 당근밭문제같은건가?? 당근밭 옆 고구마밭같은건가???

T = int(input())

for tc in range(1, T+1):
# 가로,세로길이 N  / 단어의 길이 K
    N, K = map(int, input().split())
    ARR = [list(input().split()) for _ in range(N)]
    res = 0
    for arr in ARR, zip(*ARR):
        for a in arr:
            res += ''.join(a).split('0').count('1'*K)

    print(f'#{tc} {res}')