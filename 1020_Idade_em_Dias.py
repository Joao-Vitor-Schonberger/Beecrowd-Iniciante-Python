# Lê o valor inteiro de entrada
dias_totais = int(input())

# Calcula os anos (divisão inteira por 365)
anos = dias_totais // 365

# Atualiza a variável dias_totais com o resto da divisão
dias_totais = dias_totais % 365

# Calcula os meses (divisão inteira por 30)
meses = dias_totais // 30

# O que sobra são os dias
dias = dias_totais % 30

# Imprime formatado conforme o exemplo
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")