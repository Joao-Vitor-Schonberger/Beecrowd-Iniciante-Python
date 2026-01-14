
# Lê e converte para inteiros
entrada = list(map(int, input().split()))

# Cria uma cópia ordenada
ordenados = sorted(entrada)

# Imprime os ordenados
for n in ordenados:
    print(n)

# Imprime a linha em branco obrigatória
print()

# Imprime na ordem original
for n in entrada:
    print(n)