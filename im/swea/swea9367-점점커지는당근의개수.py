import sys
sys.stdin = open("9367in.txt")

# 점점 커지는 당근의 개수

T = int(input())
for tc in range(1, T+1):
    T = int(input())
    LST = list(map(int, input().split()))

    cnt = 1 # 연속으로 커지지 않는 경우 구간의 최소 길이는 1
    cntLst = [] # 연속으로 커지는 구간을 누적할 리스트를 초기화
    for i in range(len(LST)-1): # 마지막 값 이전의 값까지...
        if LST[i]+1 == LST[i+1]: #증가하는 구간이면
            cnt += 1 # cnt를 1 늘린다
        else: # 증가하는 구간이 끝나면
            cntLst.append(cnt) # 이전 cnt값을 리스트에 넣고
            cnt = 1 # cnt 초기화
    cntLst.append(cnt) # for문 종료되었을 때 누적되어있는 cnt값도 누적해야한다

    print(f'#{tc} {max(cntLst)}') # 저장되어있는 가장 큰 구간의 값을 출력한다