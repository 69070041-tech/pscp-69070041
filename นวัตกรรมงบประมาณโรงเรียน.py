"""school inovation money identifier"""
school_name = input()
n = len(school_name)

c_first = ord(school_name[0].upper())
c_last = ord(school_name[-1].upper())

base_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

stage1 = []
for pos_idx in range(10):
    pos = pos_idx + 1
    d_p = base_digits[pos_idx]

    if pos % 2:
        val = c_first + d_p
    else:
        val = c_last - d_p

    stage1.append(val)

stage2 = []
for val in stage1:
    rem = val % n
    if rem > 9:
        rem = rem % 10
    stage2.append(rem)

stage3 = stage2[2:8]

print(*stage3)
