vitórias_inter = 0
vitórias_gremio = 0
empates = 0
total_grenais = 0

while True:
    gols_inter, gols_gremio = map(int, input().split())
    
    total_grenais += 1
    if gols_inter > gols_gremio:
        vitórias_inter += 1
    elif gols_gremio > gols_inter:
        vitórias_gremio += 1
    else:
        empates += 1
    
    print("Novo grenal (1-sim 2-nao)")
    opcao = int(input())
    
    if opcao == 2:
        break

print(f"{total_grenais} grenais")
print(f"Inter:{vitórias_inter}")
print(f"Gremio:{vitórias_gremio}")
print(f"Empates:{empates}")

if vitórias_inter > vitórias_gremio:
    print("Inter venceu mais")
elif vitórias_gremio > vitórias_inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")