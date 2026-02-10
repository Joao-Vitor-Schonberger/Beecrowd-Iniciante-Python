n = int(input())

total = 0
coelhos = 0
ratos = 0
sapos = 0

for _ in range(n):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]
    
    total += quantia
    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

p_coelhos = (coelhos / total) * 100
p_ratos = (ratos / total) * 100
p_sapos = (sapos / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {p_coelhos:.2f} %")
print(f"Percentual de ratos: {p_ratos:.2f} %")
print(f"Percentual de sapos: {p_sapos:.2f} %")