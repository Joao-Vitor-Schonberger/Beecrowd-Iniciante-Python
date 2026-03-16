import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
pos = 1

for _ in range(t):
    pa = int(input_data[pos])
    pb = int(input_data[pos+1])
    g1 = float(input_data[pos+2])
    g2 = float(input_data[pos+3])
    pos += 4
    
    anos = 0
    while pa <= pb:
        pa = int(pa + (pa * (g1 / 100)))
        pb = int(pb + (pb * (g2 / 100)))
        anos += 1
        
        if anos > 100:
            break
            
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")