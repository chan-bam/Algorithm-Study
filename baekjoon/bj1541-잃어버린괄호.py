expression = input()
res = expression.split('-')
answer = sum(list(map(int, res[0].split('+'))))
for i in range(1, len(res)):
    answer -= sum(list(map(int, res[i].split('+'))))
print(answer)

# expression = input()
# res = expression.split('-')
# answer = 0
# for i in range(len(res)):
#     if '+' in res[i]:
#         tmp = sum(list(map(int, res[i].split('+'))))
#     else:
#         tmp = int(res[i])
#     if not i:
#         answer = tmp
#     else:
#         answer -= tmp

# expression = input()
# res = expression.split('-')
#
# for i in range(len(res)):
#     if '+' in res[i]:
#         res[i] = sum(list(map(int, res[i].split('+'))))
#
# result = int(res[0])
# for j in range(1, len(res)):
#     result -= int(res[j])
#
# print(result)

'''
expression = input()

num1 = ''
num2 = ''

i = 0
while expression[i] not in '+-':
    num1 += expression[i]
    i += 1
    if i == len(expression):
        print(num1)
        exit(0)

while i < len(expression):
    if expression[i] == '-':
        k = i + 1
        while k < len(expression) and expression[k] != '-':
            if expression[k] != '+':
                num2 += expression[k]
            else:
                num1 = str(int(num1) - int(num2))
                num2 = ''
            k += 1
        num1 = str(int(num1) - int(num2))
        num2 = ''
        i = k
    elif expression[i] == '+':
        n = i + 1
        while n < len(expression) and expression[n] != '-':
            if expression[n] != '+':
                num2 += expression[n]
            else:
                num1 = str(int(num1) + int(num2))
                num2 = ''
            n += 1
        num1 = str(int(num1) + int(num2))
        num2 = ''
        i = n
print(num1)
'''