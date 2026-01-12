n1, n2, n3, n4 = map(float, input().split())

m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print(f"Media: {m:.1f}")

match m:
    case _ if m >= 7.0:
        print("Aluno aprovado.")
    
    case _ if m < 5.0:
        print("Aluno reprovado.")
    
    case _ if 5.0 <= m <= 6.9:
        print("Aluno em exame.")
        
        nota_exame = float(input())
        print(f"Nota do exame: {nota_exame:.1f}")
        
        media_final = (nota_exame + m) / 2
        
        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
            
        print(f"Media final: {media_final:.1f}")