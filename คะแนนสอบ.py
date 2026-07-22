"""score check"""
score_check_amount = int(input())
score = []
i = 0
while i < score_check_amount:
    score.append(int(input()))
    i+=1

print(max(score))
print(score.count(max(score)))
