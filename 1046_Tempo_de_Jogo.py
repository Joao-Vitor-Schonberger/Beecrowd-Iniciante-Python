i, f = map(int, input().split())

# Descibrindo se durou mais que um dia

if (f <= i):
    # Durou mais que um dia
    duracaoI = (24 - i)
    print(f"O JOGO DUROU {duracaoI + f} HORA(S)")
    
else:
    # Nâo durou mais que um dia 
    print(f"O JOGO DUROU {f - i} HORA(S)")