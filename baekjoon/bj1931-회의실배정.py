import sys
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
schedule.sort() # 시작시간으로 먼저 정렬
schedule.sort(key = lambda x:x[1]) # 종료시간 빠른순으로 정렬

e = schedule[0][1]
cnt = 1
for j in range(1, N):
    if e <= schedule[j][0]:
        e = schedule[j][1]
        cnt += 1

print(cnt)

# greedy
# 회의가 많이 열리기 위해서는 시작시간 ~ 종료시간이 짧아야 함
# 또한 이전 회의 종료 시간과 다음 회의 시작 시간 사이의 텀이 짧아야 함
# 빨리 시작하고 빨리 끝나는 회의로 구성해야 함