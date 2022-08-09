
import sys
sys.stdin = open("GNS.txt")

NUM = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for t in range(T):
    tc, lenGNS = map(str, input().split())
    GNS = input().split()
    cntLst = [0] * 10 # 카운트배열 초기화
    for g in GNS:
        for n in range(10):
            if g == NUM[n]: # NUM 리스트와 비교하여 같으면
                cntLst[n] += 1 # 동일한 인덱스의 카운트배열에 개수를 1 추가
    print(tc) # tc변수에 저장된 '#tc번호'를 먼저 출력
    for res in range(10):  # 인덱스 값을 활용하여 출력
        print((NUM[res]+' ')*cntLst[res], end=' ')  # NUM리스트의 값을 카운트배열에 저장된 값만큼 출력(end옵션 공백)
    print() # 테스트케이스 1개 끝나면 줄바꿈