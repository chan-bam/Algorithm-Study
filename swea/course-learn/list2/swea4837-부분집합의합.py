import sys
sys.stdin = open("4837in.txt")

T = int(input())

# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다(LST)

BITS = 12 # 비트연산을 할 기준 비트(원소의 개수)

LST = list(range(1, 13))

print(LST)
for tc in range(1, T+1):
    # N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수
    N, K = map(int, input().split())

    result = 0 # 부분집합의 합이 K이고 부분집합의 원소의 개수가 N개인 부분집합의 갯수를 세는 변수
    for i in range(1 << BITS): #비트의 개수(원소의 개수만큼) 비교
        cnt = 0 # 부분집합의 원소의 갯수를 세는 변수
        sumV = 0 # 부분집합의 원소의 합을 세는 변수
        for j in range(BITS): # 12비트를 비교(포함,불포함)
            if i & (1 << j): # (참이면)
                sumV += LST[j] #합산한다
                cnt += 1 #부분집합의 원소의 갯수를 센다
        if sumV == K and cnt == N:  # 부분집합의 합이 K이고 부분집합의 원소의 개수가 N개인 부분집합이 있으면
            result += 1 # 갯수를 늘린다
    print(f'#{tc} {result}')