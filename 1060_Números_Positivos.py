v = []

for i in range(6):
    entrada = float(input())
    v.append(entrada)

p = 0

for i in v:
    if (i > 0):
        p += 1
print(f"{p} valores positivos")