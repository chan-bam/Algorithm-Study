import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemons = {}

for n in range(1, N + 1):
    pokemon = input().rstrip()
    pokemons[pokemon] = str(n)
    pokemons[str(n)] = pokemon

for _ in range(M):
    print(pokemons[input().rstrip()])

# pokemons = [input().rstrip() for _ in range(N)]
#
# for _ in range(M):
#     result = input().rstrip()
#     try:
#         print(pokemons[int(result) - 1])
#     except:
#         print(pokemons.index(result) + 1)