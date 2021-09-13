
# 비밀번호 발음하기

def aeiou(word):
    for w in word:
        if w in vowel:     # tc에 모음 있을때만 true 반환
            return True
    return False

while True:
    tc = input()
    res = True       # 결과값 판단할 변수 True로 초기화
    vowel = ['a', 'e', 'i', 'o', 'u']       # 모음 리스트

    if tc == 'end':    # 들어온 문자열 'end'이면 break
        break

    if aeiou(tc) == True:        # tc에 모음 있으면
        if len(tc) >= 3:         # tc가 3글자 이상이면
            for i in range(len(tc)-2):       #  0번째부터 마지막에서 세번째까지 연속한 3개를 비교
                if tc[i] in vowel and tc[i+1] in vowel and tc[i+2] in vowel:      # 연속으로 모음이 3개 나오면
                    res = False       # 결과값 판단 변수 False로 바꾸고
                    break       # 반복문 종료
                if tc[i] not in vowel and tc[i+1] not in vowel and tc[i+2] not in vowel:      # 연속으로 모음이 아닌 글자(자음)이 3개 나오면
                    res = False       # 결과값 판단 변수 False로 바꾸고
                    break      # 반복문 종료
        if res == True:      # 위의 반복문을 끝낸 후 결과값 판단 변수가 True이면
            for i in range(len(tc) - 1):       # 첫번째 글자에서 마지막에서 2번째까지 번지를 기준으로 비교
                if tc[i] not in ['o', 'e']:
                    if tc[i] == tc[i + 1]:       # i번지의 글자와 i+1번지의 글자가 같으면
                        res = False       # 결과값 판단 변수를 False로 바꾸고
                        break      # 반복문 종료
    else:     # 모음이 없는 경우
        res = False       # 결과값 판단 변수를 False로 바꿈

    if res == True:       # 결과값 판단 변수가 True이면      # if res:로도 쓸 수 있음
        print('<{}> is acceptable.'.format(tc))
    else:      # 결과값 판단 변수가 False이면
        print('<{}> is not acceptable.'.format(tc))