import sys
sys.stdin = open("6485in.txt")

# 노선을 지나는 버스의 개수를 누적하는 함수
def bus_count(bus_stop):
    cnt = 0
    for bus in bus_line:
        if bus[0] <= bus_stop <= bus[1]:  # 버스정류장이 A이상 B 이하이니?
            cnt += 1 # 지나는 노선이면 대수를 늘린다
    # 범위 다 체크해서 cnt 다 셌으면 리스트에 저장해준다 # 버스정류장 순서대로 저장되게 된다
    bus_cnt.append(cnt)
    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # [A 이상, B 이하]
    bus_line = [list(map(int, input().split())) for _ in range(N)]
    # 두개 들어오는것도 리스트에 바로 저장할 수 있음

    P = int(input())
    # bus_stop = [int(input()) for _ in range(P)]
    bus_cnt = [] # 버스정류장별 지나는 노선 개수 누적할 변수 초기화
    for i in range(P): # 지나는지 확인해서 개수 누적해도 되므로 # 입력받으면서 비교해도 무방
        bus_count(int(input())) # 버스 노선의 순서가... 오름차순 내림차순 순서 X
    result = ' '.join(list(map(str, bus_cnt)))

    print(f'#{tc} {result}')



