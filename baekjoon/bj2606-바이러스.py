import sys
sys.stdin = open("2606in.txt")
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited.append(start)           # 시작지점(방문지점)을 visited 리스트에 추가
    for node in graph[start]:       # 그래프의 방문위치를 기준으로 연결된 노드를 기준으로 반복하여 탐색
        if node not in visited:     # 이전에 방문하지 않은 노드이면   # 이전에 방문한 노드이면 이미 바이러스가 전파된 것이므로 탐색X
            cnt += 1                # 전파된 컴퓨터의 개수를 1 늘리고
            dfs(node)               # 해당 위치를 기준으로 다시 dfs 탐색
    return cnt      # 다 탐색한 뒤 최종 누적된 cnt를 return

N = int(input())    # 컴퓨터의 개수
M = int(input())     # 연결된 간선의 개수
graph = [[] * N for _ in range(N + 1)]     # N대의 컴퓨터와 각각 연결된 컴퓨터의 정보를 2차원 배열로 저장

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)      # 무방향 그래프이기 때문에 양방향으로 다 접근하도록 양쪽에 다 연결정보를 저장
    graph[y].append(x)
# print()
cnt = 0         # 전파된 컴퓨터의 수를 저장할 변수
visited = []   # 방문여부를 체크할 visited 리스트를 생성
print(dfs(1))   # 1번 컴퓨터부터 시작해서 dfs 탐색  # 탐색이 완료되면 최종 return된 cnt값을 출력하여
                                                # 1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 개수를 출력
