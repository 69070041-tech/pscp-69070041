"""pro"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())

groups = z // x
leftover = z % x
total_paying_people = (groups * y) + leftover
total_price = total_paying_people * a

print(total_price)
