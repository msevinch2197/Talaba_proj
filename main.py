import talaba

def ortacha_baho(baholar):
    return sum(baholar) / len(baholar)

def eng_yuqori(baholar):
    return max(baholar)

def eng_past(baholar):
    return min(baholar)


baholar = [85, 90, 78, 92, 88]

res1 = talaba.ortacha_baho(baholar)
print(f"Ortacha baho: {res1}")

res2 = talaba.eng_yuqori(baholar)
print(f"Eng yuqori baho: {res2}")

res3 = talaba.eng_past(baholar)
print(f"Eng past baho: {res3}")
