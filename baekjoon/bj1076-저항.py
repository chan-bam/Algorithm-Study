import sys
input = sys.stdin.readline

resistance = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}

res1 = resistance[input().rstrip()] * 10
res2 = resistance[input().rstrip()]
mul = 10**resistance[input().rstrip()]

print((res1 + res2) * mul)