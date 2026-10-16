"""rah see check from date"""
from datetime import date

day = int(input())
month = int(input())

d = date(2000, month, day)

if d >= date(2000, 12, 22) or d <= date(2000, 1, 19):
    print("capricorn")
elif d <= date(2000, 2, 18):
    print("aquarius")
elif d <= date(2000, 3, 20):
    print("pisces")
elif d <= date(2000, 4, 19):
    print("aries")
elif d <= date(2000, 5, 20):
    print("taurus")
elif d <= date(2000, 6, 21):
    print("gemini")
elif d <= date(2000, 7, 22):
    print("cancer")
elif d <= date(2000, 8, 22):
    print("leo")
elif d <= date(2000, 9, 22):
    print("virgo")
elif d <= date(2000, 10, 23):
    print("libra")
elif d <= date(2000, 11, 21):
    print("scorpio")
else:
    print("sagittarius")
