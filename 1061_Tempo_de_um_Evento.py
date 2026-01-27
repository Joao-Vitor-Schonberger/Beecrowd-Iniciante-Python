dia_inicio = int(input().split()[1])
h1, m1, s1 = map(int, input().replace(":", "").split())

dia_fim = int(input().split()[1])
h2, m2, s2 = map(int, input().replace(":", "").split())

segundos_inicio = s1 + (m1 * 60) + (h1 * 3600) + (dia_inicio * 86400)
segundos_fim = s2 + (m2 * 60) + (h2 * 3600) + (dia_fim * 86400)

total_segundos = segundos_fim - segundos_inicio

dias = total_segundos // 86400
total_segundos %= 86400

horas = total_segundos // 3600
total_segundos %= 3600

minutos = total_segundos // 60
segundos = total_segundos % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")