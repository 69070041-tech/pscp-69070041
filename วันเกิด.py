"""wan kert chan pee nee kor pscp klub ma dai mai"""
from datetime import date

inputs = []
while len(inputs) < 6:
    for x in input().split():
        inputs.append(int(x))

person1 = date(inputs[0], inputs[1], inputs[2])
person2 = date(inputs[3], inputs[4], inputs[5])

diff = abs((person1 - person2).days)

if diff <= 7:
    print(0)
elif person1 < person2:
    print(1)
else:
    print(2)
