import sys
import tracemalloc

empt=[]
list_10=[i for i in range (1, 11)]
tuple_10=tuple(i for i in range (100, 111))
str_10='a'*10
num=5
boo=None

for i in empt, list_10, tuple_10, str_10, num, boo:
    print (sys.getsizeof(i))

################

print()
empt_2=[]
k=sys.getsizeof(empt_2)
for i in range (1, 101):
    empt_2.append(i)
    if k!=sys.getsizeof(empt_2):
        print (k, sys.getsizeof(empt_2), i)
        k=sys.getsizeof(empt_2)

######################
tracemalloc.start()
numbers = range(100_000)
snapshot=tracemalloc.take_snapshot()
# tracemalloc.stop()
# print (snapshot)
current, peak = tracemalloc.get_traced_memory()
# tracemalloc.start()
tracemalloc.reset_peak()
numbers1 = list(range(100_000))
snapshot1=tracemalloc.take_snapshot()
current1, peak1=tracemalloc.get_traced_memory()
tracemalloc.stop()
# print (snapshot1)

stats=snapshot1.compare_to(snapshot, "lineno")
print (*stats[:3], sep='\n')
print (peak/1024, peak1/1024, sep='KB ', end='KB')
