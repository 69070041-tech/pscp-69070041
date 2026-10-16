"""bonus calculate by role"""
# รับค่าและแปลงตัวอักษรตำแหน่งเป็นตัวพิมพ์ใหญ่ (.upper())
role, work_time, money = input().split()
role = role.upper()
work_time = float(work_time)
money = float(money)

# กำหนดอัตราโบนัสและเงินโบนัสคงที่ตามตำแหน่งและอายุงาน
if role == "M":
    base = 1500
    if work_time < 5:
        rate = 0.06
    elif work_time < 10:
        rate = 0.08
    else:  # ตั้งแต่ 10 ปีขึ้นไป (work_time >= 10)
        rate = 0.10

elif role == "B":
    base = 1000
    if work_time < 5:
        rate = 0.05
    elif work_time < 10:
        rate = 0.06
    else:  # ตั้งแต่ 10 ปีขึ้นไป (work_time >= 10)
        rate = 0.07

else:  # ตำแหน่ง G (พนักงาน)
    base = 500
    if work_time < 5:
        rate = 0.04
    elif work_time < 10:
        rate = 0.05
    else:  # ตั้งแต่ 10 ปีขึ้นไป (work_time >= 10)
        rate = 0.06

# คำนวณโบนัสรวม
total_bonus = (money * rate) + base
print(int(total_bonus))