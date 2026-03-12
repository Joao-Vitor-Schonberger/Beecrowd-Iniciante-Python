s = 0
num = 1
den = 1

while num <= 39:
    s += num / den
    num += 2
    den *= 2

print(f"{s:.2f}")