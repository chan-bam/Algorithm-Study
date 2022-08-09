import sys
sys.stdin = open("9829in.txt")
# 9829 고장난 전구찾기
# 안 고장난 전구 찾는 방법 (set 활용)

def check():
    # enumerate도 가능하지만 2차원 배열이므로 인덱스 활용도 가능... [i][j] 혹은... 리스트 내부에서 돌므로 [i]

    check_set = set() # 고장이 나지 않은 전구 셋 초기화 # 중복 입력 방지

    for pat in pattern:
        if pat.count(1) > half: # 가져온 pat리스트에서 1이 절반보다 많을 때 # 0상태는 고장난 전구가 아님 (1상태인 전구 중 하나가 절반을 초과했으므로 고장난 전구임)
            for idx, pt in enumerate(pat): # enumerate함수는 (인덱스,밸류) 쌍으로 리스트(혹은 셋)을 재구성해준다
                if pt == 0: # 0인 요소이면
                    check_set.add(idx+1) # 0인 것들의 인덱스번호에 1을 추가하여 셋에 입력해준다
        if pat.count(0) > half: # 가져온 pat리스트에서  0이 절반보다 많을 때 # 1인 전구는 고장난 전구가 아님 (0상태인 전구 중 하나가 절반을 초과했으므로 고장난 전구임)
            for idx2, pt2 in enumerate(pat):
              if pt2 == 1: # 1인 요소이면
                    check_set.add(idx2+1) #인덱스번호에 1을 추가하여 셋에 입력해준다

    all_idx_set = set(range(1, L + 1))  # 전체 전구번호 리스트
    return all_idx_set - check_set   # 차집합  # set에 남은 요소는 고장나지 않은 요소가 된다

T = int(input())
for tc in range(1, T+1):
    L, S = map(int, input().split())
    half = L // 2
    pattern = [list(map(int, input().split())) for _ in range(S)]
    result = check()

    print(f'#{tc}', *result)