"""bonus calculate by role"""
role, work_time, money = input().split()
work_time = int(work_time)
money = int(money)
if role == "M" :
    if work_time <= 5:
        money = (money * (6 / 100)) + 1500
    elif 5 < work_time <= 10:
        money = (money * (8 / 100)) + 1500
    else:
        money = (money * (10 / 100)) + 1500
elif role == "B" :
    if work_time <= 5:
        money = (money * (5 / 100)) + 1000
    elif 5 < work_time <= 10:
        money = (money * (6 / 100)) + 1000
    else:
        money = (money * (7 / 100)) + 1000
else:
    if work_time <= 5:
        money = (money * (4 / 100)) + 500
    elif 5 < work_time <= 10:
        money = (money * (5 / 100)) + 500
    else:
        money = (money * (6 / 100)) + 500

print(int(money))
