import sys
sys.stdin = open("2491in.txt")
T = int(input())

def solve():
    # 최대길이
    maxCnt = 0 # 최대 길이 저장
    # 연속해서 증가하는 수의 개수
    plusCnt = 1
    # 연속해서 감소하는 수의 개수
    minusCnt = 1
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            plusCnt += 1
        else:
            if plusCnt >= maxCnt:
                maxCnt = plusCnt
            plusCnt = 1
        if nums[i] >= nums[i+1]:
            minusCnt += 1
        else:
            if minusCnt >= maxCnt:
                maxCnt = minusCnt
            minusCnt = 1
    # 마지막에 센 count는 최대값과 대소비교 안되어있으므로 나와서 검사!!
    if maxCnt <= max(minusCnt, plusCnt):
        maxCnt = max(minusCnt, plusCnt)
    return maxCnt

for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    if N == 1:
        print(1) # 1일때 case를 자주 간과하게 되는듯..
    else:
        print(solve())