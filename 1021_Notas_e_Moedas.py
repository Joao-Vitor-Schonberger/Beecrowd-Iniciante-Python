v = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")

for n in notas:
    print(f"{int(v) // n} nota(s) de R$ {float(n):.2f}")
    v = v - (n * (int(v) // n))

print("MOEDAS:")

v = v * 100

for m in moedas:
    print(f"{int(v // (m * 100))} moeda(s) de R$ {float(m):.2f}")
    v = v - ((m * 100) * (v // (m * 100)))