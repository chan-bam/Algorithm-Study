A, B = map(int, input().split()) # 현재시각 A시 B분
C = int(input()) # 요리하는데 필요한 시간(분)

if B + C >= 60:
    A = (A + (B + C) // 60) % 24
    B = (B + C) % 60
else:
    B = B + C

print(A, B)

