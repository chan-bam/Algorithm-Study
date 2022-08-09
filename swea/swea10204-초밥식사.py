import sys
sys.stdin = open("10204in.txt")

# greedy

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 초밥 N접시
    susi = [list(map(int, input().split())) for _ in range(N)]

    # 선택할 차례에서 자신의 행복도를 가장 높이거나, 상대방의 행복도를 가장 낮추는 선택 중 둘중에 더 큰 경우를 선택해야함
    # 선택할 차례에 두 값의 합이 큰 값을 선택하면 자신의 행복도를 가장 높이거나 상대방의 행복도를 가장 낮추는 선택 중 더 큰 경우가 선택됨
    # 동일한 합이 있는 경우에는 어떤 값이 먼저 선택되어도 결과에 영향은X...
    # lambda 안쓰고 합을 저장해서 정렬했더니 시간초과 나서 lambda 사용..

    # 합이 큰 순으로 선택해야하므로, 합을 기준으로 내림차순 정렬
    susi.sort(key=lambda x: x[0]+x[1], reverse=True)

    result = 0   # (정연이의 행복도 - 현용이의 행복도)를 저장할 변수
    for i in range(N):
        if i % 2 == 0: # 짝수번째 -> 정연이가 고른다 : 정연이의 행복도를 더한다
            result += susi[i][0]
        else: # 홀수번째 -> 현용이가 고른다 : 현용이의 행복도를 뺀다
            result -= susi[i][1]
    print(f'#{tc} {result}')

'''
# 시간초과
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input()) 
    susi = []
    for _ in range(N):
        a, b = map(int, input().split())
        susi.append([a+b, a, b])
    susi.sort(reverse=True)
 
    result = 0   
    for i in range(N):
        if i % 2 == 0: 
            result += susi[i][1]
        else: 
            result -= susi[i][2]
    print(f'#{tc} {result}'
'''



'''
    for idx in range(N):
        a, b = map(int, input().split())
        susi.append([a, b]) # 합이 같은 경우 들어온 순서대로....
        susi_sum.append([a+b, idx])

    susi_sum.sort(reverse=True)

    # 자신의 행복도 + 상대방의 행복도 합이 다른 값보다 클 수록.......
    # 행복도의 합이 같은 경우 자신의 행복도가 높은 순이어야 함
    result = 0   # (정연이의 행복도 - 현용이의 행복도)를 저장할 변수
    for i in range(N):
        if i % 2 == 0: # 짝수번째 -> 정연이가 고른다 : 정연이의 행복도를 더한다
            result += susi[susi_sum[i][1]][0]
        else: # 홀수번째 -> 현용이가 고른다 : 현용이의 행복도를 뺀다
            result -= susi[susi_sum[i][1]][1]
    print(f'#{tc} {result}')
'''