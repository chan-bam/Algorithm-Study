import sys
input = sys.stdin.readline


word = input().rstrip()
bomb = input().rstrip()

last = bomb[-1]
len_b = len(bomb)
stk = []

for w in word:
    stk.append(w)
    if len(stk) >= len_b and stk[-1] == last:
        if ''.join(stk[-len_b:]) == bomb:
            del stk[-len_b:]
if stk:
    print(''.join(stk))
else:
    print('FRULA')