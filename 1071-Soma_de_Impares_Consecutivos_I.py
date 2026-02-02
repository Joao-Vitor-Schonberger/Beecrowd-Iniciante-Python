x = int(input())
y = int(input())

inicio = min(x, y)
fim = max(x, y)

soma = 0

for i in range(inicio + 1, fim):
    if i % 2 != 0:
        soma += i

print(soma)