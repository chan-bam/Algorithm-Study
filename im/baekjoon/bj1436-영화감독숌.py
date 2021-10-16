import sys
input = sys.stdin.readline

# 규칙 못찾겠어서 그냥 다 만들어봄...
# 시간초과 날 줄 알았는데 정답!!!

def solve():
    start = 666
    cnt = 0
    while True:
        if '666' in str(start):
            cnt += 1
            if cnt == N:
                return start
        start += 1

N = int(input())
print(solve())