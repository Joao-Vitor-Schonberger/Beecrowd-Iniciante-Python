c, q = map(int, input().split())

match c:
    case 1:
        t = float((4*q))
        print(f"Total: R$ {t:.2f}")
    case 2:
        t = float(((4.5)*q))
        print(f"Total: R$ {t:.2f}")
    case 3:
        t = float((5*q))
        print(f"Total: R$ {t:.2f}")
    case 4:
        t = float((2*q))
        print(f"Total: R$ {t:.2f}")
    case 5:
        t = float(((1.5)*q))
        print(f"Total: R$ {t:.2f}")