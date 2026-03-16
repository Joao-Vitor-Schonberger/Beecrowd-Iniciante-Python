n = int(input())

for _ in range(n):
    x = int(input())
    
    if x == 1:
        print(f"{x} nao eh perfeito")
        continue
        
    soma = 1
    limite = int(x**0.5)
    
    for i in range(2, limite + 1):
        if x % i == 0:
            soma += i
            if i != x // i:
                soma += x // i
                
    if soma == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")