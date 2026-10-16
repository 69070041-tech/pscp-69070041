"""Arcade of Time : Store Check"""

line1 = input().split()
num = int(line1[0])
check = int(line1[1])

MAXT = 1441
diff = [0] * (MAXT + 2)

for i in range(num):
    line = input().split()
    start = int(line[0])
    stop = int(line[1])
    diff[start] += 1
    diff[stop] -= 1

count = [0] * (MAXT + 2)
running = 0
for t in range(MAXT + 2):
    running += diff[t]
    count[t] = running

queries = input().split()
results = []
for i in range(check):
    k = int(queries[i])
    results.append(str(count[k]))

print(' '.join(results))
