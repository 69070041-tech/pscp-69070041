"""SEASON"""

month = int(input())
day = int(input())

if month in [3,6,9,12]:
    if day >= 21:
        if month == 3:
            SEASON = "spring"
        elif month == 6:
            SEASON = "summer"
        elif month == 9:
            SEASON = "fall"
        else:
            SEASON = "winter"

    else:
        if month == 3:
            SEASON = "winter"
        elif month == 6:
            SEASON = "spring"
        elif month == 9:
            SEASON = "summer"
        else:
            SEASON = "fall"

else:
    if month <= 2:
        SEASON = "winter"
    elif month <= 5:
        SEASON = "spring"
    elif month <= 8:
        SEASON = "summer"
    else:
        SEASON = "fall"

print(SEASON)
