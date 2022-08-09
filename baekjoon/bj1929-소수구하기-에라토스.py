# 백준 1929번
# 에라토스테네스의 체 이용


M, N = map(int, input().split())

# 에라토스테네스의 체 #############################

# 입력범위인 100만개짜리 미리 소수를 True로 하는 배열을 생성
array = [True for i in range(1000001)] # 0부터~100만까지

array[0], array[1] = False, False # 0과 1은 소수가 아니다 ! << check point!!!

for i in range(2, 1001): # 소수는 제곱근까지만 보면 되므로 (1000까지)
    if array[i]:
        for k in range(i + i, 1000001, i): # i의 배수는 소수가 아니므로 (100만까지의 수를) False로 바꿈
            array[k] = False
###############################################
# print(array)



for j in range(M, N+1):
    if array[j] == True:
        print(j)





# 구현 실패
'''
M, N = map(int, input().split())
nums = list(range(M, N+1))

print(nums)

for i in range(0, len(nums)):
    for j in range(2, int(nums[i]**0.5)+1):
        if nums[i] % j == 0:
            break
    else:
        start = i + nums[i]
        diff = nums[i]
        end = len(nums)
        for k in range(start, diff, end):
            nums[k] = False
print(nums)
'''