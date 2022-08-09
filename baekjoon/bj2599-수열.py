
# 투 포인터?
# 누적 배열 사용 # 구간의 합을 구할때 유용.. 계속 합계 안구해도 돼서 빠름

import sys
input = sys.stdin.readline

# 정수 N:온도를 측정한 전체 날짜의 수 2 이상 100,000이하
# 정수 K: 1과 N 사이의 정수 -100이상 100이하
N, K = map(int, input().split())
nums = list(map(int, input().split()))
sum_lst = [0] * (N+1) # 누적리스트는 1개 더만들어야함
for i in range(1, N+1):
    sum_lst[i] = nums[i-1] + sum_lst[i-1]
    # i번째의 누적값을 i+1에 입력하는 누적 리스트를 만듬
maxV = -10000000
for j in range(N-K+1): # 누적리스트의 값을 사용해서 K일간의 합을 빠르게 구할 수 있음..
    max_tmp = sum_lst[j+K] - sum_lst[j] # j+K인덱스의 누적값 - j번째 인덱스의 누적값 = 해당기간의 합계
    if maxV <= max_tmp:
        maxV = max_tmp
print(maxV)






















'''

N, K = map(int, input().split())
nums = list(map(int, input().split()))
sumLst = [0] * (N+1)
for i in range(1, len(nums)):
    sumLst[i] += sumLst[i-1] + nums[i-1] # 누적배열만들기....

maxV = -10000001 # 최대값 저장할 변수 나올 수 있는 숫자의 최소 숫자로 초기화
for j in range(N - K + 1): # 누적
    maxV = max(maxV, sumLst[j+K] - sumLst[j])
print(maxV)
'''
'''
N, K = map(int, input().split())
nums = list(map(int, input().split()))
maxV = 0
for i in range(N//2-K//2):
    sumV = 0
    sumV2 = 0
    # sumV += sum(nums[i:i+K])
    sumV2 += sum(nums[N-i-1-K:N-i-1])
    maxV = max(maxV, sumV, sumV2)
print(maxV)
'''

'''
N, K = map(int, input().split())
nums = list(map(int, input().split()))
sumLst = []
for i in range(N-K+1):
    sumV = 0
    sumV += sum(nums[i:i+K])
    sumLst.append(sumV)
print(max(sumLst))
'''

'''
# 시간초과
N, K = map(int, input().split())
nums = list(map(int, input().split()))
maxV = 0
for i in range(N-K+1):
    sumV = 0
    sumV += sum(nums[i:i+K])
    if maxV <= sumV:
        maxV = sumV
print(maxV)
'''
'''
# 시간초과
import sys
sys.stdin = open("2559in.txt")
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    maxV = 0
    for i in range(N-K+1):
        sumV = 0
        for j in range(K):
            sumV += nums[i+j]
        if maxV <= sumV:
            maxV = sumV
    print(maxV)
'''