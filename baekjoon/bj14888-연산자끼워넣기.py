import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split())) # N - 1개
oper = list(map(int, input().split())) # + - * / 의 개수
minV, maxV = 10**9, -10**9

def solve(depth, result):
    global minV, maxV
    if depth == N:
        minV = min(minV, result)
        maxV = max(maxV, result)
        return
    for j in range(4):
        if oper[j]:
            oper[j] -= 1
            if j == 0:
                solve(depth + 1, result + nums[depth])
            elif j == 1:
                solve(depth + 1, result - nums[depth])
            elif j == 2:
                solve(depth + 1, result * nums[depth])
            elif j == 3:
                # 음수를 양수로 나눌 때는 C++14의 기준을 따른다.
                # 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
                if result < 0:
                    temp = -(abs(result) // nums[depth])
                else:
                    temp = result // nums[depth]
                solve(depth + 1, temp)
            oper[j] += 1

solve(1, nums[0])
print(maxV)
print(minV)