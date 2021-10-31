import sys
sys.stdin = open("5948in.txt")

T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    # 서로 다른 7개의 정수 중에서 3개의 정수를 골라 합을 구해서 수를 만든다
    # 이렇게 만들 수 있는 수 중에서 5번째로 큰 수
    res = set()
    for i in range(7):
        for j in range(7):
            if i != j:
                for k in range(7):
                    if i != k and j != k:
                        res.add(nums[i] + nums[j] + nums[k])
    res_lst = list(res)
    res_lst.sort(reverse = True)
    print(f'#{tc} {res_lst[4]}')