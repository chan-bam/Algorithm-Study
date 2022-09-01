import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 이동하려고 하는 채널
M = int(input()) # 고장난 버튼의 개수
broken = input().split() # 고장난 버튼

min_cnt = abs(100 - N) # 100번에서 + - 버튼을 이동할 때의 수

for num in range(1_000_000): # 이동하려고 하는 채널 500_000보다 크면서 모든 숫자를 다 누를 수 있는 수
    for n in str(num):
        if n in broken: # 고장난 버튼이 있으면
            break
    else: # 고장난 버튼이 없으면
        min_cnt = min(min_cnt, abs(N - num) + len(str(num)))
                               # 비교하려는 숫자와의 차이 + 누른 버튼의 수
    if min_cnt == 1:
        break

print(min_cnt)









'''
import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 이동하려고 하는 채널
M = int(input()) # 고장난 버튼의 개수
broken = input().split() # 고장난 버튼

min_cnt = abs(100 - N)

for num in range(1_000_000):
    for n in str(num):
        if n in broken:
            break
    else:
        min_cnt = min(min_cnt, len(str(num)) + abs(N - num))
print(min_cnt)
'''

