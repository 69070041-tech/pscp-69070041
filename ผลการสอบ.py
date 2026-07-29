"""score pass or fail checker"""
hw = float(input())
midterm = float(input())
final = float(input())

if hw >= 5.0 and midterm >= 20.0 and final >= 25.0:
    print("pass")
else:
    print("fail")
