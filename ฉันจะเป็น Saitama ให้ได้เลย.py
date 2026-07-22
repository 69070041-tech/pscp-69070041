"""saitama workout plan creation"""

import math

target_push_up = int(input())
target_sit_up = int(input())
target_squat = int(input())
target_run = int(input())

daily_push_up = int(input())
daily_sit_up = int(input())
daily_run = int(input())
daily_squat = int(input())

day_push_up = math.ceil(target_push_up / daily_push_up)
day_sit_up = math.ceil(target_sit_up / daily_sit_up)
day_squat = math.ceil(target_squat / daily_squat)
day_run = math.ceil(target_run / daily_run)

max_day = max(day_push_up, day_run, day_squat, day_sit_up)

print(max_day)
