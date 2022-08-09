import sys
sys.stdin = open("4522in.txt")

T = int(input())

for tc in range(1, T+1):
    wrd = input()
    lenW = len(wrd)
    result = 'Exist'
    for w in range(lenW//2): # 회문검사는 중간문자를 제외한 양쪽 구간만 봐도 가능하므로..
        if wrd[w] != wrd[lenW-w-1]: # 양쪽 문자 다를때
            if wrd[w] == '?' or wrd[lenW-w-1] == '?': # 한쪽이 ?이면 회문으로 만들 수 있으므로
                continue  # 계속 반복해서 검사
            else:
                result = 'Not exist'  # 양쪽 다 문자이면 회문만들 수 없음
    print(f'#{tc} {result}')