"""wow"""
total = float(input())
max_score = float(input())

mid_plus_min = total - max_score

max_min_score = mid_plus_min / 2

if max_min_score > max_score:
    max_min_score = max_score

min_min_score = mid_plus_min - max_score

if min_min_score < 0:
    min_min_score = 0

if max_score - min_min_score > 2:
    print("Surprising")
else:
    print("Not surprising")
