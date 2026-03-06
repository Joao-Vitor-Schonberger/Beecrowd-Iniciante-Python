import sys

def resolver():
    entrada = sys.stdin.read().split()
    
    if not entrada:
        return

    A = int(entrada[0])
    
    N = 0
    for i in range(1, len(entrada)):
        valor = int(entrada[i])
        if valor > 0:
            N = valor
            break
    
    soma = 0
    for i in range(N):
        soma += A + i
        
    print(soma)

if __name__ == "__main__":
    resolver()