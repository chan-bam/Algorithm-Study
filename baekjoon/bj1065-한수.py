# 백준 1065 # 한수

N = int(input())

cnt = 0 # 한수의 개수를 셀 변수를 초기화
for i in range(1, N+1):
    tmp = i    # i를 임시변수에 대입
    hansuLst = []    # 한수를 입력할 리스트를 초기화
    while tmp >= 1:     # tmp가 1보다 클때
        hansuLst.append(tmp % 10)   # tmp를 10으로 나눈 나머지를 구해서, 1의 자리부터 한자리식 잘라서 리스트에 입력 # 1의 자리부터이므로 순서가 반대로 들어오기는 하지만 어차피 차를 구하므로 뒤집지는 않아도 됨
        tmp //= 10     # tmp를 10으로 나눈 몫을 대입하여 1의자리를 없앤 수로 다시 반복


    if len(hansuLst) <= 2:  # 한수리스트의 길이가 2보다 작으면(2자리수 이하 숫자의 한수 판별)
        cnt += 1  # 무조건 한수이므로 한수의 개수를 늘린다

    if len(hansuLst) > 2:  # 한수리스트의 길이가 2보다 크면(3자리수 이상 숫자의 한수 판별)
        flag = True     # 한수인지 아닌지를 판별할 flag값 True로 초기화
        diff = hansuLst[0] - hansuLst[1]    # 0번째값과 1번째값의 차이를 초기값으로 입력
        for j in range(1, len(hansuLst)-1):
            if diff != hansuLst[j] - hansuLst[j+1]: # 차이가 기존 차이와 다르면
                flag = False     # flag를 False로 바꾸고 반복문 종료
                break
            else:    # 차이가 초기값과 같으면
                # diff = hansuLst[j] - hansuLst[j+1]
                pass    # flag유지한 상태로 계속 반복
        if flag:     # flag가 True인 상태로 반복문이 종료되었다면
            cnt += 1     # 한수이므로 개수를 늘린다

print(cnt)
