import sys

sys.stdin = open("10163in.txt")

T = int(input())
for tc in range(1, T+1):
    # 색종이가 놓이는 평면은 가로 최대 1001칸, 세로 최대 1001칸
    # 1001 * 1001 평면
    ARR = [[0]*1002 for _ in range(1002)]

    # 색종이의 장수는 1장에서 100장까지
    N = int(input()) # 서로다른 직사각형 모양의 색종이 N장이 입력된다

    # N장별로 반복
    for n in range(1, N+1): # 배열에 n번을 입력해준다
        X1, Y1, W, H = map(int, input().split())
        for x in range(X1, X1+W):
            for y in range(Y1, Y1+H):
                ARR[x][y] = n # 배열에 n번을 입력

    # 순서대로 다 입력되었다면 # 순서대로 보이는 면적을 출력
    for m in range(1, N+1): # m(n)의 개수 세는 것이므로 바깥쪽 for문에서 유지
        cnt = 0
        for arr in ARR: # 열마다 세기 # count함수사용
            cnt += arr.count(m)
        print(cnt) # 다 셌으면 출력