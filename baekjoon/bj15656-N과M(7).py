import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def solve(answer, depth):
    if depth == m:
        print(answer.lstrip())
        # print(answer)
        return
    for i in nums:
            solve(answer + ' ' + str(i), depth + 1)
        # if answer:
        #     solve(answer + ' ' + str(i), depth + 1)
        # else:
        #     solve(str(i), depth + 1)

solve('', 0)

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = []
def perm():
    if len(res) == m:
        print(*res)
        return
    for i in nums:
        res.append(i)
        perm()
        res.pop()
perm()

'''
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러번 골라도 된다
# 중복되는 수열은 여러 번 출력하면 안된다
# 중복 순열