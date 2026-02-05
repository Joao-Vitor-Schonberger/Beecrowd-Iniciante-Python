n = int(input())

for i in range(n):
    num = int(input())
    
    if num == 0:
        print("NULL")
    else:
        if num % 2 == 0:
            resultado = "EVEN"
        else:
            resultado = "ODD"
        
        if num > 0:
            resultado += " POSITIVE"
        else:
            resultado += " NEGATIVE"
            
        print(resultado)