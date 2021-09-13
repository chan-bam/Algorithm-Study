# 백준 2941번 크로아티아 알파벳

# .count() 사용
cro_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cro_word = input()
cnt = 0
for cro in cro_lst:
    cnt += cro_word.count(cro)

print(len(cro_word)-cnt)

# cnt 글자 포함된 갯수만큼만 빼는데.. 'dz='가 3글자인데도 맞게 나오는 이유?
    # 'z='가 겹쳐서 한개를 더 세주기 때문



# .replace() 사용
cro_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cro_word = input()
cnt = 0
for cro in cro_lst:
    cro_word = cro_word.replace(cro, '*')

print(len(cro_word))