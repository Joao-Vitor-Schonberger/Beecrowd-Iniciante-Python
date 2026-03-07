x = int(input())
z = int(input())

while z <= x:
    z = int(input())

soma = 0
contagem = 0
atual = x

while soma <= z:
    soma += atual
    atual += 1
    contagem += 1

print(contagem)