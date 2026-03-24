fib = [0] * 61
fib[0] = 0
fib[1] = 1

for i in range(2, 61):
    fib[i] = fib[i-1] + fib[i-2]

t = int(input())

for _ in range(t):
    n = int(input())
    print(f"Fib({n}) = {fib[n]}")