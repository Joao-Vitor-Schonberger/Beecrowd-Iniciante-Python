a, b, c = map(float, input().split())
# print(f"a: {a}")
# print(f"b: {b}")
# print(f"c: {c}")

if (a == 0):
    print("Impossivel calcular")
else:
    delta = (b*b) - (4*a*c)
    if (delta < 0):
        print("Impossivel calcular")
    else:
        rdelta = delta ** 0.5

        x1 = ((-b) + rdelta)/(2*a)
        x2 = ((-b) - rdelta)/(2*a)

        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")
