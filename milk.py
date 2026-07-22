"""yeee"""

price = int(input())
cap_pro = int(input())
get_pro = int(input())
money = int(input())

total_bottle = money // price
caps = total_bottle

while caps >= cap_pro > 0:
    free_bottle = (caps // cap_pro) * get_pro

    total_bottle += free_bottle

    caps = (caps % cap_pro) + free_bottle


print(total_bottle)
