"""woww"""

total_score = float(input())
highest = float(input())

remaining_sum = total_score - highest

possible_mid = remaining_sum / 2

if possible_mid > highest:
    possible_mid = highest

possible_lowest = remaining_sum - highest

if possible_lowest < 0:
    possible_lowest = 0

if highest - possible_lowest > 2:
    print("Surprising")
else:
    print("Not surprising")
