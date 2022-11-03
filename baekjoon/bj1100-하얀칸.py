import sys
input = sys.stdin.readline

# board = [list(input().rstrip()) for _ in range(8)]
# (0,0) (0,2) (0,4) (0,6)
# (1,1) (1,3) (1,5) (1,7)
# ...

cnt = 0
for i in range(8):
    board = input()
    for j in range(8):
        if not (i + j) % 2 and board[j] == 'F':
            cnt += 1
print(cnt)