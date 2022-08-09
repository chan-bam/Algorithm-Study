import sys
sys.stdin = open("10912in.txt")

T = int(input())

for tc in range(1, T+1):
    wrd = input()
    lst = []
    for w in wrd:
        if w not in lst:
            lst.append(w)
        else:
            lst.remove(w)
    if len(lst) >= 1:
        lst.sort()
        result = ''.join(lst)
    else:
        result = 'Good'
    print(f'#{tc} {result}')
