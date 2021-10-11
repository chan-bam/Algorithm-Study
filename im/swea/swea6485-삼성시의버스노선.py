import sys
sys.stdin = open("6485in.txt")

# 삼성시의 버스노선

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_line = []
    for n in range(N):
        A1, B1 = map(int, input().split())
        bus_line.append([A1, B1]) # 버스노선의 지나는 범위를 리스트로 입력

    bus_lst = [] # 노선 리스트
    P = int(input())  # 노선 개수
    for p in range(P):  # 노선개수만큼 반복
        bus_lst.append(int(input())) # 노선을 리스트를 누적 # 비교해야하므로
    # print(bus_lst)

    bus_cnt = [0] * P # 노선 개수만큼의 리스트 초기화 # 지나가는 버스 노선 누적
    # print(bus_cnt)
    for b in range(len(bus_lst)): # 노선 개수만큼 범위 지정 # 인덱스를 활용
        for bus in bus_line: # 버스 노선의 지나는 범위 가져오기
            if bus[0] <= bus_lst[b] <= bus[1]: # bus_lst의 정거장이 노선의 범위 내에 있으면
                bus_cnt[b] += 1 # 지나는 노선의 개수를 1 늘린다(누적한다)
    res = ' '.join(list(map(str, bus_cnt)))  # 리스트를 공백으로 나누어 출력
    print(f'#{tc} {res}')