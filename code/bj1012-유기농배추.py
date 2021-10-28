import sys
sys.stdin = open("1012in.txt")
sys.setrecursionlimit(10**5) # 재귀 제한 바꾸기...
input = sys.stdin.readline

# 4방향
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c):
    for i in range(4):
        nr = r + dr[i] # 인접위치 4방향 탐색
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and farm[nr][nc]: # 인덱스 범위 체크 및 1인지(방문 여부) 체크
            farm[nr][nc] = 0 # 방문한 위치 0으로 바꾸고
            dfs(nr, nc)

T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    # 가로길이 # 세로길이 # 위치의 개수
    farm = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1: # 1이면 dfs
                dfs(i, j) 
                cnt += 1 # 지렁이 개수 1 추가
    print(cnt)
