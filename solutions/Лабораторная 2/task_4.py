import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

######
print()
print(gc.isenabled(), gc.get_threshold(), gc.get_count())

del first, second
print(gc.collect(), '\n')

gc.disable()
g = []
g.append(g)
del g

print(gc.collect())
gc.enable()

a, b, c = {"n": "A"}, {"n": "B"}, {"n": "C"}
a["ra"], b["ra"], c["ra"] = b, c, a
indep = {"n": "p"}

del a, b, c
print(gc.collect())
# print(indep["n"])

