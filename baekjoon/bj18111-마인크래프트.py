import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

def solution(floor, inventory):
    global min_time
    global max_floor

    time = 0
    for i in range(N):
        for j in range(M):
            height = land[i][j]
            diff = floor - height
            if time <= min_time: # time == min_time 일 때는 return 하면 안됨
                inventory -= diff
                if diff > 0:
                    time += diff
                else:
                    time += 2 * (-diff)
            else:
                return
    if inventory < 0: # 전체 다 해봤을 때 inventory가 음수가 되면 안됨
        return
    if min_time > time:
        min_time, max_floor = time, floor
    elif min_time == time and max_floor < floor:
        max_floor = floor
    return


min_time = 500 * 500 * 256
max_floor = 0

for f in range(257):
    solution(f, B)

print(min_time, max_floor)