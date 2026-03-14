n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    soma = 0
    cont = 0
    numero_atual = x
    
    while cont < y:
        if numero_atual % 2 != 0:
            soma += numero_atual
            cont += 1
        numero_atual += 1
        
    print(soma)