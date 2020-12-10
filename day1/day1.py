import itertools, math

NUM_ELEMENTS = 3
RESULT = 2020

with open('input.txt', 'r') as file:
    l = file.readlines()
    l = [ int(s) for s in l ]

for combo in itertools.combinations(l, NUM_ELEMENTS):
    if sum(combo) == RESULT:
        print(combo)
        print(math.prod(combo))
        break

