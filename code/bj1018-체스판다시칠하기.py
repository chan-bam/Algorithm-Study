# 체스판 다시 칠하기

N, M = map(int, input().split())

BRD =[list(input()) for _ in range(N)]

cntLst = []   # 횟수를 비교할 리스트 초기화 
for i in range(N-7):       # 행
    for j in range(M-7):   # 열
        # BRD[i][j]가 검은색으로 시작해야 바꿀 횟수가 적은지, 흰색으로 시작해야 바꿀 횟수가 적은지 알 수 없으므로 두 가지 경우 다 비교를 해줘야한다
        cntB = 0
        cntW = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:  # 행렬의 합이 짝수인 경우(대각선 비교)
                    if BRD[k][l] != 'B':  # 첫번째가 검은색인 기준 조건 : 첫번째가 검은색이 아닌 경우
                        cntB += 1  # 검은색으로 바꿀 횟수 추가
                    if BRD[k][l] != 'W':  # 첫번째가 흰색인 기준 조건 : 첫번째가 흰색이 아닌 경우
                        cntW += 1  # 흰색으로 바꿀 횟수 추가
                else:  # 행렬의 합이 홀수인 경우(대각선 비교)
                    if BRD[k][l] == 'B':  # 첫번째가 검은색인 기준 조건 : 두번째가 검은색인 경우
                        cntB += 1  # 흰색으로 바꿀 횟수 추가
                    if BRD[k][l] == 'W': # 첫번째가 흰색인 기준 조건: 두번째가 흰색인 경우
                        cntW += 1  # 검은색으로 바꿀 횟수 추가

        cntLst.append(cntB)   # 횟수 비교할 리스트에 추가
        cntLst.append(cntW)   # 횟수 비교할 리스트에 추가
print(min(cntLst))   # 리스트에서 가장 횟수가 적은 값을 찾기


