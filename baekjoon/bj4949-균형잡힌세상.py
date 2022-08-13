
while True:
    sentence = input()
    if sentence == '.':
        break
    else:
        world = []
        for s in sentence:
            if s in '([':
                world.append(s)
            elif s == ')':
                if world and world[-1] == '(':
                    world.pop()
                else:
                    print("no") # world.append(s)
                    break
            elif s == ']':
                if world and world[-1] == '[':
                    world.pop()
                else:
                    print("no")  # world.append(s)
                    break
        else: # 15,21행 print("no")가 아니라 word.append(s)로 처리한 경우 for ~ else 가 아니라 무조건 하단 if문으로 검사해야함
            if world:
                print("no")
            else:
                print("yes")