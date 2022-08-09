# SWEA 3143 가장 빠른 문자열 타이핑


import sys
sys.stdin = open("3143in.txt")

T = int(input())

for tc in range(1, T+1):
    wrd, w = input().split()

    cnt = 0      # wrd에 w가 포함된 갯수를 셈

    i = 0
    while i < (len(wrd) - len(w)) + 1:
        j = 0
        tmpCnt = 0       # 문자열을 찾았는지 판단할 임시 카운트
        while j < len(w): # 하단 if문 조건 and조건으로 비교하면 tmpCnt 변수가 필요하지 않다
            if wrd[i+j] == w[j]: # while문에 조건을 써주면 tmpCnt가 아닌 j와 비교해도 결과가 나옴(j변수가 증가되어 길이와 같은 값이 나오게 되므로)
                tmpCnt += 1      # 문자열 한 개 찾을때마다 카운트를 한개씩 늘린다
            j += 1
        if tmpCnt == len(w):     # while문 나왔을 때 tmpCnt가 찾는 문자열 길이와 같으면(문자열 1개 찾았으면)

            cnt += 1        # 찾은 개수 늘린다
            i += len(w)     # w 글자 길이만큼 인덱스를 증가시켜서 다음 문자열을 찾는다 # j만큼 증가시켜도 가능
        else:
            i += 1

    print(f'#{tc} {len(wrd) - (len(w)-1)*cnt}')



'''
TC = int(input())

for test_case in range(1, TC+1):
    A, B = map(str,input().split())
    cnt = 0

    A = list(A) # A만 리스트로 바꿔주기, 지우는 과정을 위해
    B = list(B)
    temp = []

    for i in range(len(A)-len(B)+1):
        if B == A[i:i+len(B)]:
            for j in range(i, i+len(B)):
                temp.append(A[j])

    cnt = 0
    if len(temp) >= len(B):
        cnt += len(temp)//len(B)

    result = len(A) - len(temp) + cnt
    print('#{} {}'.format(test_case, result))
'''