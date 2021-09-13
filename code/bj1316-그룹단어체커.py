# 1316 그룹 단어 체커

N = int(input()) # 단어 갯수

wrdLst = []  # 그룹단어를 입력할 리스트 초기화
for n in range(N):
    wrdLst.append(input())  # 그룹단어를 리스트에 입력함

    cnt = 0   # 그룹단어가 아닌 갯수를 세는 count 변수 초기화

    for w in wrdLst: # 리스트에서 그룹단어별로 확인
        wLst = []  # 그룹단어인지 판별 기준 리스트 초기화
        for i in range(len(w)): # 그룹단어의 길이 기준으로 인덱스값 기준 비교
            if len(wLst) == 0:  # 판별 기준 리스트가 비어있으면
                wLst.append(w[i])  # i번 인덱스의 글자를 입력
            if w[i] != wLst[-1] and w[i] in wLst: # i번 인덱스의 글자가 마지막인덱스의 글자와 다르고, 판별할 리스트에 있으면
                cnt += 1 # cnt 증가
                break # for문 종료
            else:
                wLst.append(w[i]) # 위 조건에 해당하지 않으면 판별 기준 리스트에 추가한다
print(N - cnt) # 그룹단어의 개수에서 - 그룹단어가 아닌 cnt를 제외한 갯수를 출력한다