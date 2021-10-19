def click(now):
    if switch[now]:
        switch[now] = 0
    else:
        switch[now] = 1
    return

N = int(input())

switch = ['*'] + list(map(int, input().split()))
          # 패딩 감안..

students = int(input())
stuLst = []
for i in range(students):
    st, num = map(int, input().split())

    if st == 1: # 남학생
        for j in range(num, len(switch), num): # 배수..... 바꾸기....
            click(j)
    else: # 여학생  # 받은 스위치를 기준으로 인접한 영역 중에서 좌우 대칭인 구간
        click(num)
        for k in range(1, N//2):
            if num - k < 0 or num + k >= len(switch):
                break  # 좌우로 절반 이하만 가보면 되는데... # 범위 벗어났을때.. 반복문 종료 해야한다!!
            if switch[num-k] == switch[num+k]: # 좌우로 대칭인지
                click(num-k)
                click(num+k)
            else:
                break ## 범위 안벗어났지만 대칭이 아닐 때는 반복문 종료해줘야한다.....!!!
                      # 이 부분을 잡아내는데 오래걸렸음...
switch.pop(0) # 0번 스위치 제거
for k in range(0, N, 20): # 20개씩 줄바꿈해서 출력!!
    print(*switch[k:k+20])
