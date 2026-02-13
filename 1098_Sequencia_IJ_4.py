i = 0
while i <= 2:
    for j_base in range(1, 4):
        j = j_base + i
        
        if i == int(i) or round(i, 1) == int(round(i, 1)):
            print(f"I={int(round(i, 1))} J={int(round(j, 1))}")
        else:
            print(f"I={round(i, 1):.1f} J={round(j, 1):.1f}")
            
    i += 0.2