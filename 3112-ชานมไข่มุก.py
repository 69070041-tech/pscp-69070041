"""boba tea cal calculate"""

BOBA_CAL = {'H': 5, 'O': 3}

TEA_CAL = {
    'R': {1: 12, 2: 18, 3: 25},
    'T': {1: 15, 2: 20, 3: 30},
}

boba, boba_gram = input().split()
tea, sweet, tea_cc = input().split()

boba_cal = BOBA_CAL.get(boba, 2)
tea_cal = TEA_CAL.get(tea, {1: 10, 2: 15, 3: 20}).get(float(sweet), 20)

total_cal = (float(boba_gram) * boba_cal) + (int(tea_cc) * tea_cal)

print(int(total_cal) if total_cal.is_integer() else total_cal)
