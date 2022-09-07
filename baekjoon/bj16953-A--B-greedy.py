A, B = map(int, input().split())

cnt = 1
while B != A:
    tmp = B
    if B % 10 == 1:
        B //= 10
    elif not B % 2:
        B //= 2
    cnt += 1
    if tmp == B: # 두 연산 모두 못 거치는 경우
        cnt = -1
        break
print(cnt)