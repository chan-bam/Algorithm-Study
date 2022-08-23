import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cloth = {}
    N = int(input())
    for _ in range(N):
        name, type = input().rstrip().split()
        cloth[type] = cloth.get(type, 0) + 1
    case = 1
    for c in cloth.values():
        case *= c + 1
    print(case - 1)







'''
for _ in range(T):
    N = int(input())
    cloth = {}
    for _ in range(N):
        name, type = input().rstrip().split()
        cloth[type] = cloth.get(type, 0) + 1

    case = 1
    for c in cloth.values():
       case *= (c + 1) # (선택할 수 있는 갯수 + 아무것도 선택하지 않는 경우)
    print(case - 1)
                # 모두 선택하지 않는 경우 제외
'''