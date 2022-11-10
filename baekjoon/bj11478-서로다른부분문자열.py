import sys
input = sys.stdin.readline

S = input().rstrip()
result = set()
for i in range(len(S)): # 부분문자열의 길이
    for j in range(len(S) - i):
        result.add(S[j:j + i + 1])
print(len(result))