import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()
len_w, len_b = len(word), len(bomb)
stk = []
i = 0
while True:
    if len(stk) >= len_b and ''.join(stk[-len_b:]) == bomb:
        for j in range(len_b):
            stk.pop()
    elif i < len_w:
        stk.append(word[i])
        i += 1
    else:
        break
if stk:
    print(*stk, sep='')
else:
    print('FRULA')

'''
# 시간초과
import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()

while bomb in word:
    word = ''.join(word.split(bomb))

if len(word):
    print(word)
else:
    print('FRULA')
'''