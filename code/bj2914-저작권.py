A, I = map(int, input().split()) # 앨범에 수록된 곡의 개수 A. 평균값 I

# 멜로디의 평균값 = 저작권이 있는 멜로디의 개수 / 앨범에 수록된 곡의 개수
# 24 = ? / 38
# 평균값은 소수점 첫째자리에서 올림한 값
# 적어도 몇 곡이 저작권이 있는 멜로디인지

print(A * (I - 1) + 1)
