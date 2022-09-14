import sys
input = sys.stdin.readline

text1, text2 = input().rstrip(), input().rstrip()
N, M = len(text1), len(text2)
LCS = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if text1[i - 1] == text2[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[N][M])


'''
import sys
input = sys.stdin.readline

text1, text2 = input().rstrip(), input().rstrip()
N, M = len(text1), len(text2)

# LCS(Longest Common Subsequence, 최장 공통 부분 수열)
LCS = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if text2[i - 1] == text1[j - 1]: # 알파벳이 같은 경우
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else: # 알파벳이 다른 경우
            LCS[i][j] = max(LCS[i][j - 1], LCS[i - 1][j])

print(LCS)
print(LCS[-1][-1])
'''