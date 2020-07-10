"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import itertools
#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
l = 4


def f(x):
    return x * 4 + 6

# Your code here

values = {}
#compute all double combinations and store
for x in q:
    for y in q:
        val = f(x) + f(y)
        if val not in values:
            values[val] = []
        values[val].append((x, y, True))
        val = f(x) - f(y)
        if val not in values:
            values[val] = []
        values[val].append((x, y, False))

for x in list(values):
    tuples = values[x]
    if len(tuples) > 1:
        if tuples[0][2] ^ tuples[1][2]:
            print(f"{tuples[0][0:2]} and {tuples[1][0:2]}")


