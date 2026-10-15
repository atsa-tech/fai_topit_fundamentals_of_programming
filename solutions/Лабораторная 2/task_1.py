#Эксперимент A
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

#Эксперимент B

first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

first = [10, 20]
second = [10, 20]

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second, first==second, first is second)
print(id(first), id(second))

# Практическое задание

import copy

p1 = ["base", ["alex"], ["old"]]
t1 = p1

t1[2].append("new")
t1[0] = "more"

print("p1:", p1)
print("t1:", t1)

p2 = ["base", ["alex"], ["old"]]
t2 = copy.deepcopy(p2)

t2[2].append("new")
t2[0] = "more"

assert p2 is not t2

print("p2:", p2)
print("t2:", t2)
