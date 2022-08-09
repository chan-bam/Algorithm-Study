import sys
sys.stdin = open("1860in.txt")

T = int(input())

for tc in range(1, T+1):
    # N명, M초, K개
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort() # 정렬

    res = 'Possible'
    for i in range(len(customer)):
        if customer[i] // M * K - i - 1 < 0: #인덱스를 방문인원수로 활용 # 현재초까지 누적 판매량에서 방문인원수를 뺐을때 음수가 되면 못파는 상태임
            res = 'Impossible'
            break
    print(f'#{tc} {res}')


'''
    for i in range(0, maxT+1):
        if i > 0 and i % M == 0:
            bread += K
        if i in customer:
            if bread >= 1:
                bread -= 1
            else:
                res = 'Impossible'
                break
    print(f'#{tc} {res}')
'''