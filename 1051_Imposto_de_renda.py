v = float(input())

if 0 <= v <= 2000.00:
    print("Isento")

elif 2000.00 < v <= 3000.00:
    imposto = (v - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")

elif 3000.00 < v <= 4500.00:
    imposto = 80.00 + (v - 3000.00) * 0.18
    print(f"R$ {imposto:.2f}")

else: # Acima de 4500
    imposto = 350.00 + (v - 4500.00) * 0.28
    print(f"R$ {imposto:.2f}")