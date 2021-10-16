import sys
sys.stdin = open("7568in.txt")

# N명
N = int(input())

body = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * N

# 기준학생보다 키도 더 크고 몸무게도 더 큰 사람의 명수를.. 학생의 인덱스와 동일한 인덱스를 사용하는 카운트베열을 만들어서 센다
for i in range(len(body)):
    for j in range(1, N):
        if body[i][0] < body[(i+j) % N][0] and body[i][1] < body[(i+j) % N][1]: # circuler하게 값을 가져와야 할 때는 mod 연산이 유용!
            cnt[i] += 1
# 등수는 +1

for c in cnt:
    print(c+1, end=' ')