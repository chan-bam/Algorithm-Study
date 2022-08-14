# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
input = sys.stdin.readline

N = int(input())

nums = [int(input()) for n in range(N)]
nums = sorted(nums)

cnt_dic = {}
length = len(nums)
sum_val = 0

for n in nums:
    sum_val += n
    if n in cnt_dic:
        cnt_dic[n] += 1
    else:
        cnt_dic[n] = 1

# 산술평균
print(int(round(sum_val / length, 0)))

# 중앙값
print(nums[length // 2])

max_cnt = 0
# 최빈값
for key, value in cnt_dic.items():
    if max_cnt < value:
        max_cnt = value
        freq = [key]
    elif max_cnt == value:
        freq.append(key)
if len(freq) == 1:
    print(freq[0])
else:
    freq.sort()
    print(freq[1])

# 범위
print(nums[-1] - nums[0])