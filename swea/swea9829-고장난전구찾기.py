import sys
sys.stdin = open("9829in.txt")
# 9829 고장난 전구찾기

# 데이터 많으면 시간초과날 것 같은데..?

# 2차원배열로 해보자... # 함수화
def check():
    cnt = [0] * L
    for patt in pattern:
        for i in range(L):
            pat = patt[:] # 2차원리스트는 내부에서 바꿔주는 수밖에...
            if pat[i] == 1:
                pat[i] = 0
            else:
                pat[i] = 1
            if pat.count(1) != half:
                cnt[i] += 1
    return cnt.index(0)+1

T = int(input())
for tc in range(1, T+1):
    L, S = map(int, input().split())
    # 전구의 수 L , 패턴의 수 S
    half = L // 2
    pattern = [list(map(int, input().split())) for _ in range(S)]
    result = check()
    print(f'#{tc} {result}')

'''
T = int(input())
for tc in range(1, T+1):
    L, S = map(int, input().split())
    # 전구의 수 L , 패턴의 수 S
    half = L // 2
    cnt = [0] * L
    for s in range(S):
        pattern = list(map(int, input().split()))
        for i in range(L):  # 패턴마다 한자리씩 모두 다 바꿔본다
            pat = pattern[:]  # 리스트 초기화(복사)---원래상태에서 바꿔줘야 하므로
            if pat[i] == 1:  # 1이면 0으로
                pat[i] = 0
            else:  # 0이면 1으로 바꿔본다
                pat[i] = 1
            if sum(pat) != half:    # 바꿨을 때 1의 개수가 절반이 아닌 전구상태일때
                cnt[i] += 1     # 해당 전구의 인덱스를 인덱스로 하는 카운트배열에 누적
    # 패턴마다 모두 반복해서 전구를 바꿔봤을때 한번도 절반이 아닌 적이 없는 전구(카운트가 0)가 고장난 전구의 인덱스이다

    result = cnt.index(0)+1 # 0인 개체의 인덱스를 찾는다  # 인덱스 0부터이므로 1 추가해준다
    print(f'#{tc} {result}')
'''
'''
# 반대로 생각하기
T = int(input())
for tc in range(1, T+1):
    L, S = map(int, input().split())
    # 전구의 수 L , 패턴의 수 S
    half = L // 2
    cnt = [0] * L
    for s in range(S):
        pattern = list(map(int, input().split()))
        for i in range(L):  # 패턴마다 한자리씩 모두 다 바꿔본다
            pat = pattern[:]  # 리스트 초기화(복사)---원래상태에서 바꿔줘야 하므로
            if pat[i] == 1:  # 1이면 0으로
                pat[i] = 0
            else:  # 0이면 1으로 바꿔본다
                pat[i] = 1
            if sum(pat) != half:    # 바꿨을 때 1의 개수가 절반이 아닌 전구상태일때
                cnt[i] += 1     # 해당 전구의 인덱스를 인덱스로 하는 카운트배열에 누적
    # 패턴마다 모두 반복해서 전구를 바꿔봤을때 한번도 절반이 아닌 적이 없는 전구(카운트가 0)가 고장난 전구의 인덱스이다

    result = cnt.index(0)+1 # 0인 개체의 인덱스를 찾는다  # 인덱스 0부터이므로 1 추가해준다
    print(f'#{tc} {result}')

'''
'''
T = int(input())
for tc in range(1, T+1):
    L, S = map(int, input().split())
    # 전구의 수 L , 패턴의 수 S
    half = L // 2
    cnt = [0] * L
    for s in range(S):
        pattern = list(map(int, input().split()))
        for i in range(L):  # 패턴마다 한자리씩 모두 다 바꿔본다
            pat = pattern[:]  # 리스트 초기화(복사)---원래상태에서 바꿔야 하므로
            if pat[i] == 1:  # 1이면 0으로
                pat[i] = 0
            else:  # 0이면 1으로 바꿔본다
                pat[i] = 1
            if sum(pat) == half:    # 바꿨을 때 1의 개수가 절반(정상적인 전구상태)일때
                cnt[i] += 1     # 해당 전구의 인덱스를 인덱스로 하는 카운트배열에 누적
    # 패턴마다 모두 반복해서 전구를 바꿔봤을때 세번 다 절반상태가 되는 전구 카운트배열의 인덱스가 고장난 전구의 번호-1이다

    result = cnt.index(S)+1
    print(f'#{tc} {result}')

'''

'''
T = int(input())
for tc in range(1, T+1):
    L, S = map(int, input().split())
    # 전구의 수 L , 패턴의 수 S
    half = L // 2   # 정상적인 전구 상태는 절반만 바뀌어야 함
    cnt = [0] * L   # 전구를 바꾸었을 때 정상적인 전구상태가 되는 경우를 세는 카운트배열을 만든다
    for s in range(S):  # 입력되는 패턴마다 반복
        pattern = list(map(int, input().split())) # 1개의 패턴을 입력받는다
        for i in range(L):  # 모두 다 바꿔본다
            pat = pattern[:]    # 리스트 초기화(복사)--원래상태에서 바꿔야 하므로
            if pat[i] == 1:     # 1이면 0으로
                pat[i] = 0
            else: # 0이면 1으로 바꿔본다
                pat[i] = 1
            if sum(pat) == half:    # 바꿨을 때 1의 개수가 절반(정상적인 전구상태)일때
                cnt[i] += 1     # 해당 전구의 인덱스를 인덱스로 하는 카운트배열에 누적
    # 패턴마다 모두 반복해서 전구를 바꿔봤을때 세번 다 절반의 전구만 켜진 상태가 되는 전구의 인덱스가 고장난 전구의 번호-1이다

    for k in range(L):
        if cnt[k] == S:
            result = k+1 # 카운트배열에 저장된 수가 패턴의 수 S와 일치(해당 전구를 바꿨을때 모두 정상적인 전구가 되는 경우)하는 인덱스+1를 반환
            break # 찾았으면 break

    print(f'#{tc} {result}')
'''


