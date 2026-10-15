import sys
import tracemalloc

def peak(obj):
    tracemalloc.start()
    tracemalloc.reset_peak()

    if obj=="list":
        res= list(range(100_000))
    else:
        res=range(100_000)

    size=sys.getsizeof(res)
    length = len(res)
    now, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return length, size, now/1024, peak/1024

len_1, list_size, list_now, list_peak, =peak("list")
len_2, range_size, range_now, range_peak = peak("range")

coef=list_peak/range_peak

print(f"list: Число элементов: {len_1} | Размер: {list_size} б | Текущий {list_now} | Пик: {list_peak:.2f} КБ")
print(f"range: Число элементов: {len_2} | Размер: {range_size} б | Текущий {range_now} | Пик: {range_peak:.2f} КБ")
print(f"Отношение пиковых объемов {coef:.1f}")
