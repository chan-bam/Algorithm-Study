# 셀프넘버

notSelfLst = []     # 셀프넘버 아닌 숫자를 저장할 리스트
n = 1               # 1부터
while n < 10000:    # 9999까지 셀프넘버가 아닌 것을 계산함
    tmp = n  # n을 직접 계산하면 while문 조건에 영향을 주므로 tmp변수에 옮겨서 값을 계산
    notSelfNum = n   # 일단 n을 미리 더한 값으로 초기화

    # n과 각 자리수를 더해야하므로 10의 나머지를 이용하여 구함
        # --- 10의 나머지를 구하는 부분이 잘 떠오르지 않았음...
    while tmp >= 1:     # tmp가 1보다 클 때까지만 반복
        notSelfNum += (tmp % 10)    # tmp + 10으로나눈 나머지(1의자리 수 한자리)를 더함
        tmp //= 10      # tmp를 10으로 나누어서 몫을 저장해주고 반복(이미 더한 1의자리수는 볼 필요 없으므로)
    # print(n, ',', notSelfNum)
    notSelfLst.append(notSelfNum)   # 최종 계산된 셀프넘버가 아닌 숫자를 저장함
    n += 1    # 1을 증가시킨 후 반복

for i in range(1, 10001):    # 1부터 10000까지의 숫자중에서
    if i not in notSelfLst:    # 셀프넘버가 아닌 수 리스트에 없을 때
        print(i)   # 셀프넘버이므로 출력