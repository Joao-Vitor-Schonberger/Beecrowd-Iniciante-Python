while True:
    try:
        valores = input().split()
        
        x = int(valores[0])
        y = int(valores[1])
        
        if x == 0 or y == 0:
            break
        
        # Verificação dos quadrantes
        if x > 0 and y > 0:
            print("primeiro")
        elif x < 0 and y > 0:
            print("segundo")
        elif x < 0 and y < 0:
            print("terceiro")
        elif x > 0 and y < 0:
            print("quarto")
            
    except EOFError:
        break