"""Arcade of Time : Store Check"""
num, check = map(int, input().split())

diff = [0] * 1445
i = 0
for i in range(num):
    start, stop = map(int, input().split())
    diff[start] += 1
    diff[stop] -= 1

open_stores = [0] * 1445
current_open = 0
for minute in range(1442):
    current_open += diff[minute]
    open_stores[minute] = current_open

check_times = list(map(int, input().split()))

results = []
for i in range(check):
    k = check_times[i]
    results.append(str(open_stores[k]))

print(" ".join(results))
