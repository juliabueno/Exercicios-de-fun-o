def pn(n):
    if n > 0:
        print('Positivo')
    elif n == 0:
        print('Nulo')
    else:
        print('Negativo')

print('Positivo ou Negativo')
n = int(input('digite um numero: '))
print('Esse numero é', end=' ')
pn(n)