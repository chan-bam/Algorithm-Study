import sys
sys.stdin = open("4047in.txt")

T = int(input())

for tc in range(1, T+1):
    wrd = input()
    cntLst = [[0]*14 for _ in range(4)] # 카운트배열 만들기
    SDHC = ['S', 'D', 'H', 'C'] # 각각의 문자 유무와 카운트배열 인덱스에 활용
    resLst = [] # 결과 개수 카운팅하여 입력
    result = '' #초기화 # 에러 아닌경우 빈문자열

    for i in range(0, 3, len(wrd)): # 문자까지 비교해도 결과에는 지장 없지만...
        if wrd[i] in SDHC:
            if wrd[i+1] == 0: # 0으로 시작하는 경우 # 한글자만 가져와서 카운트 인덱스에 활용
                cntLst[SDHC.index(wrd[i])][int(wrd[i+2])] += 1 # 슬라이싱 범위에 주의
            else: # 0으로 시작하지 않는 경우 두글자 다 가져와서 정수로 카운트 인덱스에 활용
                cntLst[SDHC.index(wrd[i])][int(wrd[i+1:i+3])] += 1
    for cnt in cntLst:
        resLst.append(13 - sum(cnt)) # 부족한 개수를 일단 먼저 센다  # 함수를 활용했으면 구조 달라졌을 것.. 지금도 뒤에서 셀 수는 있지만 break 두번하는거 별로라..
        for j in cnt: # 2개 이상인 것이 있으면
            if j >= 2:
                result = 'ERROR' # 에러
                break
    if result != 'ERROR': # 문자열이 에러 아니면
        result = ' '.join(list(map(str, resLst))) # 센 개수를 공백문자로 묶어서 리스트로
    print(f'#{tc} {result}')

