# 백준 1292번 : 쉽게 푸는 문제

A, B = map(int, input().split())

seq = []
i = 1
while len(seq) < B:
    for j in range(0, i):
        seq.append(i)
    i += 1

seqSlice = seq[A-1:B]

print(sum(seqSlice))


'''
def makeSquence():
    lst = []
    for i in range(1, B):
        for j in range(0, i):
            lst.append(i)
            if len(lst) == B:
                return lst

seq = makeSquence()
seqSlice = seq[A-1 : B]
print(sum(seqSlice))
'''

