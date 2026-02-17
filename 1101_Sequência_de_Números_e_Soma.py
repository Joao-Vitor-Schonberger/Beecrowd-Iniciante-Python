while True:
    try:
        valores = list(map(int, input().split()))
        
        if len(valores) < 2:
            break
            
        m, n = valores
        
        if m <= 0 or n <= 0:
            break
        
        menor = min(m, n)
        maior = max(m, n)
        
        soma = 0
        sequencia = ""
        
        for i in range(menor, maior + 1):
            sequencia += str(i) + " "
            soma += i
            
        print(f"{sequencia}Sum={soma}")
        
    except EOFError:
        break