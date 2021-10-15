import sys
sys.stdin = open("8810in.txt")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    goguma = list(map(int, input().split()))

    cntV = 0    # 큰 고구마 줄기의 개수

    sumV = goguma[0] # 줄기당 고구마 개수의 합계 초기화 : 첫번째 값으로 초기화

    g_cnt = 1   # 큰 고구마 줄기의 길이(영역 수)는 1개로 초기화 # 일단 한 영역을 세고 시작하므로
    maxG = 0    # 고구마 줄기의 가지 수 중 가장 긴 값을 비교할 변수 초기화
    maxS = 0    # 가장 긴 줄기에 달린 고구마의 개수(긴 줄기가 여러개라면 고구마의 개수가 많은 쪽)를 비교할 변수 초기화


    # 고구마줄기의 영역 구분법 : 이전 값보다 증가하는 값이 아니거나, 이전값보다 증가했지만 마지막 인덱스인 경우
    # 마지막에 범위의 최솟값 0이나 범위를 벗어나는 값 -1을 추가해서 비교한다면....?

    for i in range(1, N):   # 1번 인덱스부터 비교
        if goguma[i-1] < goguma[i]:     # i-1번째 고구마의 개수보다 i번째 고구마의 개수가 더 크면(증가하면)
            if i == N-1:    # 인덱스의 마지막인 경우
                sumV += goguma[i]   # 해당 영역의 고구마의 개수를 누적한다
                g_cnt += 1      # 영역의 길이를 누적한다
                cntV += 1   # 큰 고구마줄기의 개수를 1늘린다
                # 한 영역 다 셌으므로 최대값 비교
                if g_cnt > maxG:    # 줄기(영역)의 길이가 기존에 비교한 큰 고구마 줄기 영역의 길이보다 큰 경우 # 영역의 길이가 긴 고구마의 개수를 출력하므로
                    maxG = g_cnt    # 줄기의 최대 길이 갱신
                    maxS = sumV     # 현재 누적된 고구마의 개수로 가장 길이가 긴 줄기에 달린 최대값 갱신
                elif g_cnt == maxG:     # 줄기의 길이가 기존에 비교한 큰 고구마 줄기 영역의 길이와 같은 경우
                    if maxS < sumV:     # 현재 누적된 고구마의 개수가 같은 길이의 고구마의 개수보다 크면
                        maxS = sumV     # 큰 고구마줄기의 고구마 개수의 최대값으로 갱신
            else:   # 마지막인덱스의 값이 아닌 경우
                sumV += goguma[i]   # 영역에 포함된 고구마의 개수를 누적한다
                g_cnt += 1      # 영역의 길이를 누적한다

        else:   # 증가하는 값이 아닌 경우: 영역의 마지막 값이 인덱스의 마지막이 아닌 경우
            if g_cnt > 1:   # 영역의 길이가 2 이상인 경우 (영역의 길이가 1이면 큰 고구마줄기의 개수로 세지 않는다)
                cntV += 1       # 기존 영역 다 셌으므로 # 큰 고구마줄기의 개수를 늘린다
                # 한 영역 다 셌으므로 최대값 비교
                if g_cnt > maxG:    # 고구마줄기 영역의 길이가 기존에 저장된 줄기 길이보다 큰 경우
                    maxG = g_cnt    # 고구마줄기 길이 갱신
                    maxS = sumV     # 긴 고구마줄기에 포함된 고구마 개수 갱신
                elif g_cnt == maxG:     # 고구마줄기 영역의 길이가 기존에 저장된 줄기 길이와 같은 경우
                    if maxS < sumV:     # 저장된 고구마줄기의 개수가 더 큰 경우
                        maxS = sumV     # 고구마줄기 개수의 최대값으로 갱신
            sumV = goguma[i]    # 다음영역으로 넘어왔으므로 sumV의 초기값을 갱신
            g_cnt = 1   # 영역의 개수를 1로 초기화
    # 출력할 값은... 긴 고구마줄기의 개수와 가장 긴 고구마줄기에 포함된 고구마의 개수... # 가장 긴 고구마줄기가 두개 이상인 경우 더 많은 고구마의 개수
    print(f'#{tc} {cntV} {maxS}')

'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    goguma = list(map(int, input().split()))
    tmp_goguma = [goguma[0]]
    cntV = 0
    lenDic = {}

    for i in range(1, N):
        if goguma[i-1] < goguma[i]:
            if i == N-1:
                cntV += 1
                tmp_goguma.append(goguma[i])
                if len(tmp_goguma) in lenDic.keys():
                    if lenDic[len(tmp_goguma)] <= sum(tmp_goguma):
                        lenDic[len(tmp_goguma)] = sum(tmp_goguma)
                else:
                    lenDic[len(tmp_goguma)] = sum(tmp_goguma)
            else:
                tmp_goguma.append(goguma[i])
        else:
            if len(tmp_goguma) > 1:
                if len(tmp_goguma) in lenDic.keys():
                    if lenDic[len(tmp_goguma)] <= sum(tmp_goguma):
                        lenDic[len(tmp_goguma)] = sum(tmp_goguma)
                else:
                    lenDic[len(tmp_goguma)] = sum(tmp_goguma)
                cntV += 1
            tmp_goguma = [goguma[i]]
    print(f'#{tc} {cntV} {lenDic[max(lenDic)]}')


'''




'''
for tc in range(1, T+1):
    N = int(input())

    # 고구마
    goguma = list(map(int, input().split()))

    maxV = 0 # 가장 긴 줄기에 달린 고구마의 수
    sumV = goguma[0] # 줄기에 달린 고구마의 수를 누적할 변수
    cntV = 0 # 줄기의 개수
    g_cntV = 0
    tmp_goguma = [goguma[0]]
    print(tmp_goguma)

    for i in range(1, N):
    # 고구마의 개수

        if goguma[i-1] < goguma[i]:
            sumV += goguma[i]
            tmp_goguma.append(goguma[i])
            if i == N: # i가 i-1보다 크고(증가하는 수이고) 마지막값이면
                cntV += 1
        else:
            if sumV > goguma[i-1]: # 고구마 개수 1개일때는 안 셈
                cntV += 1
            if len(tmp_goguma) > maxV:
                maxV = len(tmp_goguma)
                maxSum = sum(tmp_goguma)
            sumV = goguma[i]
            tmp_goguma.clear()
            tmp_goguma.append(goguma[i])


    print(f'#{tc} {cntV} {maxSum}')
'''