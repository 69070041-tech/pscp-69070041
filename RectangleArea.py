"""Rectangle area overlapping checker"""

x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

x1_max, y1_max = x1 + w1, y1 + h1
x2_max, y2_max = x2 + w2, y2 + h2

overlap_width = min(x1_max, x2_max) - max(x1, x2)
overlap_height = min(y1_max, y2_max) - max(y1, y2)

if overlap_width > 0 and overlap_height > 0:
    area = overlap_width * overlap_height
    print(area)
else:
    print("no overlapping")
