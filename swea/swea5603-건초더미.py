# 건초더미
import sys
sys.stdin = open("5603.txt")

# N개의 건초더미
# 원래는 모든 건초더미의 크기가 같았는데, 위치가 바뀌어서 크기가 달라짐
# 바뀐 건초더미들이 주어졌을때
# 건초를 몇번 움직여야 다시 모두 같게 만들 수 있을지 구하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 건초더미 갯수
    grass = []  # 건초더미의 높이를 입력받을 리스트 초기화
    for size in range(N):  # 건초더미 갯수만큼 반복
        grass.append((int(input())))  # 건초더미의 높이를 리스트에 입력받음

    avgV = sum(grass) // N  # 건초더미 높이의 평균을 구함

    difSum = 0 # 건초더미의 평균과 각 높이의 차이를 누적 합산할 변수를 초기화
    for g in grass:  # 건초더미 각각의 높이마다 비교하기 위해 반복
        if g <= avgV:  # 비교한 건초더미의 높이가 평균값보다 작으면
            difSum += (avgV - g)   # 평균값에서 건초더미의 높이를 뺀 차이값을 합산한다
        else:  # 비교한 건초더미의 높이가 평균값보다 크면
            difSum += (g - avgV)   # 건초더미의 높이에서 평균값을 뺀 차이값을 합산한다
        # abs함수로 절대값을 구해서 합산할 수도 있음
    print(f'#{tc} {difSum // 2}')   # 차이 값이 최종 누적 합산된 변수의 값에서 나누기 2를 하면 옮긴 횟수가 나온다



## 아래는 코드는 시간초과가 발생함.. 건초더미의 개수가 최대 10000개인데 비교를 많이 해야해서 그런듯?
# for tc in range(1, T+1):
#     N = int(input())
#     grass = [] # 건초더미의 높이를 입력받을 리스트 초기화
#     for size in range(N):
#         grass.append((int(input()))) # 건초더미의 높이를 리스트에 입력받는다
#
#     maxIdx = grass.index(max(grass)) # 가장 높은 건초더미의 인덱스를 찾는다
#     minIdx = grass.index(min(grass)) # 가장 낮은 인덱스의 인덱스를 찾는다
#
#     cnt = 0 # 횟수를 셀 변수 초기화
#     while grass[minIdx] != grass[maxIdx]: # 가장 높은 건초더미의 갯수와 가장 낮은 건초더미의 갯수가 같지 않을 때만 반복
#         grass[maxIdx] -= 1 # 가장 높은 건초더미의 갯수를 1 줄인다
#         grass[minIdx] += 1 # 가장 낮은 건초더미의 갯수를 1 늘린다
#         cnt += 1 # 횟수를 1 늘린다
#         maxIdx = grass.index(max(grass)) # 가장 높은 건초더미값의 인덱스를 다시 구한다
#         minIdx = grass.index(min(grass)) # 가장 낮은 건초더미값의 인덱스를 다시 구한다
#     print(f'#{tc} {cnt}')
