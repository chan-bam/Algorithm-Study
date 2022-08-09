# SWEA 4865 # 글자수

import sys
sys.stdin = open("4865in.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = set(input())  # 중복생략
    str2 = list(input())

    strDic = {}

    for s in str1:
        strDic[s] = str2.count(s)

    print(f'#{tc} {max(strDic.values())}')