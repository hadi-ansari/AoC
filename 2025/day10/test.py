from z3 import *

a, b, c, d, e, f = Ints("a b c d e f")

opt = Optimize()

opt.add(e + f == 3)
opt.add(b + f == 5)
opt.add(c + d + e == 4)
opt.add(a + b + d == 7)

opt.add(a >= 0, b >= 0, c >= 0, d >= 0, e >= 0, f >= 0)

total = a + b + c + d + e + f
opt.minimize(total)

opt.check()
model = opt.model()

print("Minimum total usage:", model.evaluate(total))
for v in [a, b, c, d, e, f]:
    print(v, "=", model[v])
