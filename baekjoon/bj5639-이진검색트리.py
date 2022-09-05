import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

graph = []

def dfs(start, end):
    # 시작과 끝 값이 역전시 리턴
    if start > end:
        return

    # 시작값보다 더 큰 값이 없는 경우(오른쪽 서브트리 없는 경우) 대비
    mid = end + 1

    for i in range(start + 1, end + 1):
        # 루트보다 크면 오른쪽 서브트리
        if graph[start] < graph[i]:
            mid = i
            break

    dfs(start + 1, mid - 1) # 왼쪽 서브트리
    dfs(mid, end) # 오른쪽 서브트리
    print(graph[start])


while True:
    try:
        x = int(input())
        graph.append(x)
    except:
        break

dfs(0, len(graph) - 1)