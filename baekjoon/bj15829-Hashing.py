N = int(input())

text = input()

result = 0

for i in range(N):
    result += (ord(text[i]) - 96) * 31 ** i

print(result % 1234567891)