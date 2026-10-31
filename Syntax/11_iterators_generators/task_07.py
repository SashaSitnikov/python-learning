import time
import sys

print(sys.getsizeof([x * x for x in range(10**6)])) # 8448728
print(sys.getsizeof((x * x for x in range(10**6)))) # 208

start = time.perf_counter()
x = sum([x * x for x in range(10**6)])
end = time.perf_counter()
print(f"{end - start:.2f}") # 0.08

start_two = time.perf_counter()
y = sum((x * x for x in range(10**6)))
end_two = time.perf_counter()
print(f"{end_two - start_two:.2f}") # 0.05