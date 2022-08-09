# 16922  # 로마 숫자 만들기

# XXXV:35(10+10+10+5)
# IXI = 1+10+1

# 사용할 수 있는 숫자의 종류 " I:1, V:5, X:10, L:50 "
N = int(input())     # 숫자의 개수

romeLst = []    # 만들어진 숫자를 입력할 리스트 초기화

for i in range(N + 1):  # i는 숫자50을 사용하는 개수: 범위 "0개 ~ N개"
    for j in range(N + 1 - i):  # j는 숫자10을 사용하는 개수: 범위 "0개 ~ N-i개" (50의 개수 i개는 이미 사용하여 사용할 수 없으므로)
        for k in range(N + 1 - (i + j)):    # k는 숫자5를 사용하는 개수: 범위 "0개 ~ N-(i+j)개" (50의 개수 i개와 10의 개수 j개는 이미 사용하여 사용할 수 없으므로)
            m = N - (i + j + k)  # m은 1을 사용하는 개수 : 범위 "0개 ~ N-(i+j+k)개" (50의 개수 i개, 10의 개수 j개, 5의 개수 k개는 이미 사용하여 사용할 수 없으므로)
            sumV = 1*m + 5*k + 10*j + 50*i   # 숫자마다 해당 숫자를 사용한 개수를 곱한 값을 합한 값이 만들어진 숫자
            if sumV not in romeLst:  # 중복된 숫자(이미 입력되어있는 숫자)는 입력하지 않음
                romeLst.append(sumV)     # 리스트에 중복된 숫자가 없으면 만들어진 숫자를 입력

print(len(romeLst)) # 만들어진 숫자가 최종 입력된 리스트의 개수를 출력








'''
# 부분집합은 한번씩만 썼을때만.. 구하기 때문에 부분집합으로 풀 수 없는 문제

for i in range(1 << 4):
    sumV = 0
    for j in range(4):
        if i & 1 << j:
            # print(romeNum[j], end=',')
            sumV += romeNum[j]
            print(sumV)
        resSet.add(sumV)

print(resSet)
'''