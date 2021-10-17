import sys
sys.stdin = open("2564in.txt")
input = sys.stdin.readline

# 절대거리 기준으로 구하자..!

# 0,0기준으로 시계방향으로 상점과 동근이의 거리를 구해놓고..
# (시계방향 거리) 구하기
# 반시계방향 거리 : (전체거리 - 시계방향거리) 구하기
# 시계방향 거리 - 동근이 시계방향거리 <-> [ 반대쪽으로 가는 거리 : 둘레 - (시계방향 거리-동근이시계방향 거리) ] 를 비교하여 짧은 거리를 result로

# 방향
# 1 : 북쪽    # 2: 남쪽     # 3: 서쪽     # 4: 동쪽

# 시계방향 거리
def clock_dist(dir, pos):
    if dir == 1: # 북쪽이면
        return pos
    elif dir == 2: # 남쪽이면
        return w + h + w - pos
    elif dir == 3: # 서쪽이면
        return w + h + w + h - pos
    else: # 동쪽이면
        return w + pos


# 일단 인풋
w, h = map(int, input().split())

cir = (w+h)*2 # 전체 둘레 # 반시계방향의 거리를 구할때 필요...

N = int(input())    # 상점의 개수

store = [list(map(int, input().split())) for _ in range(N)]

g_dir, g_pos = map(int, input().split())

# 일단 동근이의 시계방향 거리를 # 기준으로 구한다
guard_clock = clock_dist(g_dir, g_pos) # 동근이의 시계방향 거리

result = 0
for s in store:
    dist = abs(guard_clock - clock_dist(s[0], s[1])) # 0,0을 기준으로 한 동근이의 시계방향 거리 - 0,0 기준 가게의 시계방향 거리 
    dist_rev = cir - dist # 전체 둘레에서 시계방향 거리를 빼주면!!! 반대쪽으로 도는 방향 거리가 나옴
    result += min(dist, dist_rev) # 시계방향 거리 <-> 반대쪽으로 도는 방향 거리 중 적은 값 (최소거리)를 result에 누적한다

print(result)