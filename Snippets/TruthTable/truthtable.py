
import itertools

# formula = "A and B or C and D"
# formula = "not (A and B)"
formula = "not ((not (A and B)) and (not (A and B)))"

vars = sorted(set([c for c in formula if c.isupper()]))

print(formula + "\n" + "-" * len(formula))

for vs in itertools.product((0, 1), repeat=len(vars)):
    tr = str.maketrans({var: str(v) for var, v in zip(vars, vs)})
    f = formula.translate(tr)
    print(f, "|", int(eval(f)))
