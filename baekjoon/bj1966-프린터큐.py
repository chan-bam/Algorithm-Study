import sys
input = sys.stdin.readline

T = int(input())

def solution(find_idx, que):
    cnt = 0
    # result = []
    while que:
        if 1 < len(Q):
            for other_number in Q[1:len(Q)]:
                if que[0][0] < other_number[0] : # 값 비교
                    que.append(que.pop(0))
                    break
            else:
                cnt += 1
                res = que.pop(0)
                # result.append(que.pop(0))
                if res[1] == find_idx: # index값이 찾는 index값과 같으면
                    return cnt
        else:
            cnt += 1
            res = que.pop(0)
            # result.append(que.pop(0))
            if res[1] == find_idx:
                return cnt
    return(cnt)

for _ in range(T):
    N, M = map(int, input().split()) # N:문서의 개수, M: Queue에서 몇번째 놓여 있는지
    Q = list(map(int, input().split()))
    Q = [[Q[idx], idx] for idx in range(len(Q))] # [값, index]
    # print(Q)
    print(solution(M, Q))

