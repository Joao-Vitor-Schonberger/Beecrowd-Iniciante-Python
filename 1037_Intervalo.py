v = float(input())

match v:
    case _ if v < 0 or v > 100:
        print("Fora de intervalo")
    case _ if 0 <= v <= 25:       # Intervalo [0, 25]
        print("Intervalo [0,25]")
    case _ if 25 < v <= 50:       # Intervalo (25, 50]
        print("Intervalo (25,50]")
    case _ if 50 < v <= 75:       # Intervalo (50, 75]
        print("Intervalo (50,75]")
    case _ if 75 < v <= 100:      # Intervalo (75, 100]
        print("Intervalo (75,100]")