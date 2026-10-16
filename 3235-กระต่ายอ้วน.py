"""fattest rabbit"""
rabbit = int(input())

over_weight = 0
max_weight = 0
fattest_name = ""

for _ in range(rabbit):
    name,weight = input().split()
    weight = int(weight)
    if weight > 15:
        over_weight+=1

    if weight > max_weight:
        fattest_name = name
        max_weight = weight

print(over_weight)
print(f"{fattest_name}")
