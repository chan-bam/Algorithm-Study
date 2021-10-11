BULB = list(map(str, input()))

target = ['N'] * len(BULB)

cnt = 0
for i in range(len(BULB)):
    if BULB[i] != target[i]:
        for j in range(i, len(BULB), i+1):
            if BULB[j] == 'N':
                BULB[j] = 'Y'
            else:
                BULB[j] = 'N'
        cnt += 1
    elif BULB == target:
        break
print(cnt)