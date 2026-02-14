int(input())

for _ in range(n):
    valores = list(map(int, input().split()))
    x = valores[0]
    y = valores[1]
    
    inicio = min(x, y)
    fim = max(x, y)
    
    soma_impares = 0
    
    for i in range(inicio + 1, fim):
        if i % 2 != 0:
            soma_impares += i
            
    print(soma_impares)