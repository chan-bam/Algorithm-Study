from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

cards = deque([i + 1 for i in range(N)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)