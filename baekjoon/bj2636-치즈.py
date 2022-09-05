import sys
# sys.stdin = open("2636in.txt")
sys.setrecursionlimit(10**5) # 최대 재귀 깊이 늘리기
input = sys.stdin.readline

def dfs(x, y):
    global cnt
    r, c = x, y
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr < n and nc >= 0 and nc < m:
            if visited[nr][nc] != 1:    # 방문을 안한 곳이면.. # not이 더 빠르다고 한다 # 불리언 판단이 더 빠르다고 한다
                visited[nr][nc] = 1     # 방문체크
                if arr[nr][nc] == 1:    # 1이면  # 그냥 :<-으로 쓰는 불리언 판단이 더 빠르다고 한다
                    arr[nr][nc] = 0     # 1인 영역은 0으로 만들고 dfs는 X
                    cnt += 1  # 0에 인접한 1 개수 세기
                    # 원래 1이었으므로 dfs는 하지 않지만, 0으로 값이 치환되고, visited에 방문체크했으므로 안쪽의 1은 dfs를 하지 않게되어
                    # 0인 테두리 안에 인접해있는 1만 값을 0으로 바꾸게됨 -- 0이 되었으므로 다음 while문에서 dfs했을때 dfs로 방문하게됨
                else: # 방문을 했고 0이면
                    dfs(nr, nc)  # 인접영역 dfs 탐색


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

hour = 0 # 치즈가 모두 녹아서 없어지는데 걸리는 시간
while True:
    visited = [[0] * m for _ in range(n)] # visited가 while문을 돌 때마다 초기화되므로 기존에 치즈(1)였다가 0으로 바뀐 좌표도 다시 탐색을 하게 됨
    # visited[0][0] = 1  # (0,0)부터 dfs 탐색 -> 방문체크
    cnt = 0  # 한 번 dfs 돌 때마다 1 개수를 카운트할 변수
    dfs(0, 0)

    if cnt == 0:      # 1의 개수가 0개가 되었을 때 -> 다 돌아서 치즈가 없는 상태 일 때
        result = cheese     # cnt의 개수가 0이 되기 직전에 센 1의 개수가, 녹기 한시간 전에 남아있는 개수가 되므로 result 변수에 저장하고
        break   # while문 빠져나오기
    else:       # 치즈가 남아있으면
        hour += 1     # 시간을 1 늘림
        cheese = cnt  # 위에서 시행한 dfs 함수에서 센 1의 개수를  cheese 변수에 저장

print(hour)      # 치즈가 모두 녹아서 없어지는데 걸리는 시간 출력
print(result)    # 모두 녹기 한시간 전에 남아있는 치즈 조각이 놓여 있는 칸의 개수 출력
