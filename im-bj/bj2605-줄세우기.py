# 백준 2605 - 줄세우기 (IM테스트 대비문제) # 브론즈2

# 코드 수정
stLen = int(input())
stLst = list(map(int, input().split()))
resLst = [1] # 줄 서는 순서에 따라 맨 처음에는 0번째자리에 1이 오게 되어있으므로 1을 최초요소로 하는 리스트를 초기화하여 생성

for i in range(1, stLen):
    # resLst[i -stLst[i]]이전의 값 + (i+1) + resLst[i - stLst[i]] 이후의 값으로 리스트 재구성
    resLst = resLst[0:i-stLst[i]] + [i+1] + resLst[i-stLst[i]:]

print(' '.join(list(map(str, resLst)))) # 리스트 요소를 공백을 사이에 두고 출력



'''
# 최초 제출 코드

stLen = int(input())
stLst = list(map(int, input().split()))
resLst = []

for i in range(stLen):
    if len(resLst) == 0: #리스트 비어있으면
        resLst.append(i+1) # 1번값 입력...
    else:
        # resLst[i -stLst[i]]이전의 값 + (i+1) + resLst[i - stLst[i]] 이후의 값으로 리스트 재구성
        resLst = resLst[0:i-stLst[i]] + [i+1] + resLst[i-stLst[i]:]
        # print(resLst)

print(' '.join(list(map(str, resLst)))) # 리스트를 공백을 사이에 두고 출력
'''