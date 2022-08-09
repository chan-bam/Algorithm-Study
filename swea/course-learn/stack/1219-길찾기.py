import sys
sys.stdin = open("1219in.txt")

for _ in range(10):
    tc, N = map(int, input().split())
    # N 순서쌍의 개수 # 시작정점, 도착정점 순...
    road = list(map(int, input().split()))
    Glst = [[] for _ in range(100)] # 0부터 99까지 인접리스트 정점의 개수 # 2차원..
    for i in range(N):
        Glst[road[2*i]].append(road[2*i+1])
    visited = [0]*100
    ans = 0
    stk = [0] # 0에서 시작하므로 0으로 스택 초기화

    while stk: # 스택 비어있지 않으면
        v = stk.pop(-1) # 스택에서 꺼내서 v에 넣고
        if v == 99:
            ans = 1
            break
        if visited[v]: # 이미 방문했다면...
            continue
        visited[v] = 1
        for i in Glst[v]:
            if not visited[i]:
                stk.append(i) # 스택에 인접한 위치 넣고

    print('#{} {}'.format(tc, ans))
