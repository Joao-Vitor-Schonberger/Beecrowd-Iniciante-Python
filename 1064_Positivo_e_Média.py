quantidade_positivos = 0
soma_positivos = 0

for _ in range(6):
    valor = float(input())
    
    if valor > 0:
        quantidade_positivos += 1
        soma_positivos += valor

media = soma_positivos / quantidade_positivos

print(f"{quantidade_positivos} valores positivos")
print(f"{media:.1f}")