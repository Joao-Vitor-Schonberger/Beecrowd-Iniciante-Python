def resolver():
    novo_calculo = 1
    
    while novo_calculo == 1:
        notas_validas = []
        
        while len(notas_validas) < 2:
            nota = float(input())
            
            if 0 <= nota <= 10:
                notas_validas.append(nota)
            else:
                print("nota invalida")
        
        media = sum(notas_validas) / 2
        print(f"media = {media:.2f}")
        
        while True:
            print("novo calculo (1-sim 2-nao)")
            novo_calculo = int(input())
            
            if novo_calculo == 1 or novo_calculo == 2:
                break

resolver()