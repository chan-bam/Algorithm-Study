# 네 번째 점
# 직사각형이기 때문에 가로, 세로 좌표가 동일한 좌표가 두번씩 나오게 된다

xLst = []
yLst = []
result = ''
for tc in range(3):
    x, y = map(int, input().split())
    xLst.append(x)
    yLst.append(y)

for x in xLst:
    if xLst.count(x) == 1:   ## x좌표 중 한 번만 나오는 숫자 찾기
        result += str(x)     # x = str(x)

for y in yLst:
    if yLst.count(y) == 1:   ## y좌표 중 한 번만 나오는 숫자 찾기
        result += (' ' + str(y))     # y = str(y)

print(result)     # print(x, y)  ## sep option 기본값 ' ' 공백문자이므로.... 두개의 변수를 출력하면 공백문자를 사이에 두고 출력하게 된다

'''
xLst = []
yLst = []
for tc in range(3):
    x, y = map(int, input().split())
    xLst.append(x)
    yLst.append(y)

for x in xLst:
    if xLst.count(x) == 2:
        xLst.remove(x)
        xLst.remove(x)

for y in yLst:
    if yLst.count(y) == 2:
        yLst.remove(y)
        yLst.remove(y)

print(' '.join(map(str, xLst + yLst)))
'''