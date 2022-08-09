N = int(input())
words = [[] for _ in range(51)]
for _ in range(N):
    word = input()
    if word not in words[len(word)]: # 같은 단어 여러번 입력된 경우 한번만
        words[len(word)].append(word) 

for w in words:
    w.sort() # 길이 같은 경우 사전순 정렬
    for i in w:
        print(i)