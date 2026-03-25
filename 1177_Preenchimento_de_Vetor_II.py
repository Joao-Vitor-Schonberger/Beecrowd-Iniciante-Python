t = int(input())
n = []

for i in range(1000):
    n.append(i % t)
    print(f"N[{i}] = {n[i]}")