n = int(input())

for _ in range(n):
    try:
        line = input().split()
        if not line: break 
        x = int(line[0])
        y = int(line[1])
        
        if y == 0:
            print("divisao impossivel")
        else:
            result = x / y
            print(f"{result:.1f}")
            
    except EOFError:
        break