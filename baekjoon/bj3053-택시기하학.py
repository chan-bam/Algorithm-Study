from math import pi

R = int(input())

# 유클리드 기하학 원의 넓이
u = R ** 2 * pi
# 택시 기하학 원의 넓이
t = R ** 2 * 2

print('{:.6f}'.format(u))
print('{:.6f}'.format(t))