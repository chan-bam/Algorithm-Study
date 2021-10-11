import sys
sys.stdin = open("6190in.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    maxV = 0 # 최대값

    for i in range(N):
        for j in range(i+1, N):
            multi = numbers[i]*numbers[j] # 수끼리 곱한 값
            # 단조 증가하는 수인가 유무 판단?
            multi_str = str(multi)
            for k in range(len(multi_str)-1):
                if int(multi_str[k]) > int(multi_str[k+1]):
                    break
            else:  # 조건이 거짓(0--길이가 0이라서 실행이 안되거나)이거나 break에 한번도 안걸렸을 때 실행하는 구문
                maxV = max(maxV, multi) # 반복문 다 돌았을 때
            # if len(multi_str) >= 2: # 숫자가 2자리수 이상일 때만 max값 찾도록...
            #     for k in range(len(multi_str)-1):
            #         if int(multi_str[k]) > int(multi_str[k+1]):
            #             break
            #         if k == len(multi_str)-2: # 마지막 인덱스까지 다 돌았을 때
            #             maxV = max(maxV, multi)
    if maxV > 0:
        res = maxV
    else:
        res = -1
    print(f'#{tc} {res}')
