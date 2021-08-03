
### 2050 알파벳을 숫자로 변환

# alpha = input()

# alpha_dic = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 
#             'H' : 8, 'I' : 9, 'J': 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14,
#             'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21,
#             'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

# for a in alpha:
#     print(alpha_dic[a], end =' ')


### 2046 스탬프 찍기

# number = int(input())
# print(number*'#')


### 2043 서랍의 비밀번호

# p, k = map(int, input().split())

# if p > k:
#     result = p - k + 1
# elif k > p:
#     result = k - p + 1
# else: 
#     result = 0

# print(result)

### 2029 몫과 나머지 출력하기

# T = int(input())
# for test_case in range(1, T + 1):
#     a, b = map(int, input().split())
#     print(f'#{test_case} {a//b} {a%b}')

### 2025 N줄 덧셈

number = int(input())
total = 0

for i in range(1, number+1):
    total += i

print(total)