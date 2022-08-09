# 백준 2775 부녀회장이 될테야

T = int(input())

for tc in range(T):
    K = int(input())  # 층
    N = int(input())  # 호

    lst = []
    arr = [[0]*N for _ in range(K+1)]

    # print(arr)
    for i in range(K+1):    # 층  # 0층부터 있기 때문에 K층까지
        for j in range(N):  # 호  # 호수는 1호부터 있음
            if i == 0:  # 0층일때만
                arr[i][j] = j+1 # j+1을 입력
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
                                    # j=0 -> j-1 == -1 -1층 데이터 없으나.. 에러 안나는 이유:
                                                # 파이썬은 음수인덱스가 있어서..!! 마지막값으로 입력되어있는 0을 더하게 됨

    # print(arr)
    print(arr[i][j])

#################
## 참조 사항
# 요점
# 0층 1 2 3 4 5 6 ----
# 1층 1 3 6 10 15 21 ----
# 2층 1 4 10 20 35 56 ----
# 이라는 수열을 가진다
# 이 수열의 점화식은
# d[i][j] = d[i-1][j] + d[i][j-1]
# 이것을 코드로 작성하면 된다