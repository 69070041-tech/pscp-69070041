"""paper size finder"""

r, h, glue_length = map(float,input().split())

paper_width = h + (2 * r)

paper_length = ((2 * 3.14) * r) + glue_length

print(f"{paper_width:.2f} {paper_length:.2f}")
