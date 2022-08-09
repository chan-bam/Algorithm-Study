import sys
sys.stdin = open("2116in.txt")
# 어차피 옆면은 돌릴 수 있으므로 최대값을 가져오고
# 위 아래 값을 잘 가져와서 합계를 구할 때 잘 삭제해주는 것이 이 문제의 핵심....
# 주사위는 중복되는 숫자가 없으므로 remove를 할 수 있는데 인덱스가 변경되기 때문에 제거하는 순서가 중요함
# 미리 다음 주사위의 아랫면의 값이 될 윗면 값 저장해 놓고 삭제해야함...


N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0} # 위 인덱스, 아래 인덱스 쌍

result = []
for i in range(6): # 아래 주사위의 6면을 기준으로 함 # i는 아랫면의 인덱스
    sumLst = []     # sum으로 누적해도 되긴 함
    tmp = list(range(1, 7)) # 1~6까지 리스트 만듬
    next = dice[0][rotate[i]]    # 첫번째 주사위의 윗면의 숫자를 저장 # 다음 주사위의 아랫면이 됨
    tmp.remove(dice[0][i]) # 아랫면 삭제
    tmp.remove(next) # 윗면 삭제
    sumLst.append(max(tmp)) # 남은 숫자(옆면의 숫자)중에서 가장 큰 값이 최댓값을 만드는데 활용됨
    for j in range(1, N):
        tmp = list(range(1, 7))
        tmp.remove(next) # 아랫면 삭제
        next = dice[j][rotate[dice[j].index(next)]] # 윗면 값 저장 # 다음 주사위의 아랫면이 됨
        tmp.remove(next) # 윗면 삭제
        sumLst.append(max(tmp)) # 대소 비교이므로 값 누적해도 됨..
    result.append(sum(sumLst)) # 대소 비교이므로 값 누적해도 됨..
print(max(result)) # 저장되어 있는 값 중 가장 큰 값













'''
N = int(input()) # 주사위의 개수
# 주사위는 숫자 1~6 한번씩만 나오고 중복이 없다
# 위 아래 인덱스의 규칙은 딱히 없다... 그냥 문제에서 정해져있을뿐 ㅠㅠ

dice = [list(map(int, input().split())) for _ in range(N)]

rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0} # 딕셔너리로 주사위의 아렛면에 따른 윗면 저장 # 리스트로 저장해도 같은 활용이 가능하나...

maxV = 0
for i in range(6): # 첫 번째 주사위를 기준으로 1~6까지 모두 순회
                   # i인덱스를 아랫면 기준으로 하여 윗면을 정하고 옆면의 최댓값을 더하기
    sumV = 0 # 옆면의 최댓값 누적할 변수

    tmp = list(range(1, 7)) #[1, 2, 3, 4, 5, 6] # 주사위 각 면에 써져있는 1~6
    tmp.remove(dice[0][i]) # 주사위 아랫면의 숫자 제거
    next = dice[0][rotate[i]] # 첫번째 주사위의 윗면 값 계산 # 현재 인덱스의 맞은편 인덱스.... 0번인덱스일때는  5번숫자를 삭제
    tmp.remove(next) # 첫번째 주사위의 윗면 값 삭제
    sumV += max(tmp) #첫번째 주사위의 윗면 아랫면을 제외한 숫자중에 최대값을 더한다

    for j in range(1, N):
        tmp = list(range(1, 7))
        tmp.remove(next) # 아래 주사위의 윗면 제거
        next = dice[j][rotate[dice[j].index(next)]] # 현재주사위의 윗면 계산
        tmp.remove(next) # 현재 주사위의 윗면 제거
        sumV += max(tmp) # 현재 주사위의 옆면들 중 가장 큰 값 누적
    maxV = max(maxV, sumV) # 최대값 비교하여 저장

print(maxV)
'''