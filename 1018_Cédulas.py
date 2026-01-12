n = int(input())

# N (0 < N < 1.000.000)

centena_de_milhar = n // 100000
dezena_de_milhar = n // 10000
unidade_de_milhar = n // 1000
centena = n // 100
dezena = n // 10
unidade = n // 1

print(f'{centena_de_milhar} centena(s) de milhar')
print(f'{dezena_de_milhar} dezena(s) de milhar')
print(f'{unidade_de_milhar} unidade(s) de milhar')
print(f'{centena} centena(s)')
print(f'{dezena} dezena(s)')
print(f'{unidade} unidade(s)')


