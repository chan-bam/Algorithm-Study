N = int(input())

for i in range(1, 65):
    # print(2**i)
    if N < 2**i:
        res = 2**(i+1) - N - 2**i
        break
# print(res)
for j in range(0, 65):
    if 2**j == res:
        res2 = j
        break
# print(res2)

print(i - res2)