from collections import Counter
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

# dictionary
def solution_dic():
    result = {}
    for c in cards:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    for f in find_cards:
        if f in result:
            print(result[f], end=' ')
        else:
            print('0', end=' ')

# Counter
def solution_counter():
    result = Counter(cards)
    for f in find_cards:
        if f in result:
            print(result[f], end=' ')
        else:
            print('0', end=' ')

# bisect
def solution_bisect():
    cards.sort()
    for f in find_cards:
        print(bisect_right(cards, f) - bisect_left(cards, f), end = ' ')

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
find_cards = list(map(int, input().split()))
# solution_dic()
# solution_counter()
solution_bisect()