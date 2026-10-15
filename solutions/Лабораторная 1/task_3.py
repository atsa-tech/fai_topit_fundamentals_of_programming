import math
x, y = 17, 5
print (x+y, x-y, x*y, x/y, x//y, x%y, x**y, '\n', 2 ** 1000)
result = 0.1+0.2
print (result, result==0.3, result-0.3, math.isclose(result, 0.3))

m=[int("42"),
float("3.14"),
str(2026),
bool(0),
bool(-1),
bool(""),
bool("False"),
complex(2, -3)]

for i in m:
    print (i, type(i))

print( m[-1].real, m[-1].imag)