def hanoi(n, start, end):
    if n == 1: # base_case
        print(start, end)
        return
    else:
        hanoi(n - 1, start, 6 - start - end)
        print(start, end)
        hanoi(n - 1, 6 - start - end, end)

N = int(input())
print(2**N - 1)
hanoi(N, 1, 3)