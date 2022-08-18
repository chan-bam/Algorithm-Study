from math import sqrt
N = int(input())

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if distance == 0 and r1 == r2:
        print(-1) # 동심원
    elif distance == abs(r1 - r2) or distance == r1 + r2:
        print(1) # 내접, 외접
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2) # 두점에서 만남
    else:
        print(0)






'''
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 원의 방정식 이용하여 두 터렛의 거리 구하기
    distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    # 동심원이고 반지름이 같을 때
    if distance == 0 and r1 == r2:
        print(-1)
    # 내접 또는 외접일 때 (한점만 접함)
    elif distance == abs(r1 - r2) or distance == r1 + r2:
        print(1)
    # 서로 다른 두 점에서 만날 때
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)
    # 그 외
    else:
        print(0)
'''

