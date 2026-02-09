n = []

for i in range(100):
    add = int(input())
    n.append(add)

m = max(n)
p = n.index(m)

print(m)
print(p + 1)