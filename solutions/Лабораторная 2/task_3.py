import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

###########

import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

###########

a, b, c = {1}, {2}, {3}
reg = weakref.WeakValueDictionary({'r1': a, 'r2': b, 'r3': c})

print(list(reg.keys()))

del c
print(list(reg.keys()))

del b
print(list(reg.keys()))
