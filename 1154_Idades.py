soma = 0
contagem = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    soma += idade
    contagem += 1

media = soma / contagem
print(f"{media:.2f}")