import sys
sys.stdin = open("2477in.txt")

# 한번씩만 연속으로 나오는 긴 변의 위치를 찾아서 곱한 값에서
# 그거보다 3개 떨어져있는 짧은변의 위치를 찾아서 곱한 값을 빼주면 밭의 면적인 것이 핵심!!

K = int(input())
field = [list(map(int, input().split())) for _ in range(6)]
# 카운트배열
# 변의 방향을 인덱스로 나오는 개수를 센다
cnt = [0] * 4 # 방향은 동서남북 4방향... # 5로 해서 0번인덱스 안쓰는게 인덱싱이 더 편하게 된다
# 한번 나오는 인덱스의 개수
for i in range(6):   # d, w in arr: 해서 d만 가져오는 방법도....
    cnt[field[i][0]-1] += 1

mul = 1
mul_p = 1
# 긴변의 곱은 찾았는데...
for i in range(len(field)):
    if cnt[field[i][0]-1] == 1: # 한번씩만 나온 방향이면 -> 긴변
        mul *= field[i][1] # 곱해준다
        mul_p *= field[(i+3)%6][1] # 한번씩만 나온 숫자의 3칸씩 뒤 위치에 있는데 인덱스 튀어나가지 않고 다시 앞에서부터 circular하게 가져오도록 mod연산을 해준다


print((mul - mul_p) * K)