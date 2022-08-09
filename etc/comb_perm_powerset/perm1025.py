
def perm(n, k):
    if n == k: # 순열의 길이와 k가 같아지면 종료
        print(t)
    else:
        for i in range(N):
            if visited[i] == 0: # 방문하지 않았으면
                visited[i] = 1 # 방문표시
                t[k] = a[i] # 순열에 입력
                perm(n, k+1) # 0에서 시작해서 1씩 추가
                visited[i] = 0 #방문표시 풀기

a = [1, 2, 3]
N = len(a)
t = [0] * N # 순열을 생성할 때 사용
visited = [0] * N
perm(N, 0)