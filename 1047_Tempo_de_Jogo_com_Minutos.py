hi, mi, hf, mf = map(int, input().split())

# 1. Converter tudo para minutos totais desde o início do dia
inicio_total_min = (hi * 60) + mi
fim_total_min = (hf * 60) + mf

# 2. Calcular a duração em minutos
duracao_min = fim_total_min - inicio_total_min

# 3. Ajustar caso o jogo tenha virado a noite ou durado 24h completas
# Se a duração for menor ou igual a 0, significa que passou da meia-noite 
# ou completou 24h exatas (ex: 7 7 7 7). Somamos 24h em minutos (1440).
if duracao_min <= 0:
    duracao_min += 24 * 60

# 4. Converter de volta para horas e minutos
horas = duracao_min // 60  # Divisão inteira para achar as horas
minutos = duracao_min % 60 # O resto da divisão são os minutos

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")