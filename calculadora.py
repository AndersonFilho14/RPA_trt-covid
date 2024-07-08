n1 = int(input('Primeiro numero que vc deseja: '))
n2 = int(input('Segundo numero que vc deseja: '))
o = input('Operador (+, -, *, /): ')

if o == '+':
    print(f'Resultado: {n1+n2}')
elif o == '-':
    print(f'Resultado: {n1-n2}')
elif o == '*':
    print(f'Resultado: {n1*n2}')
else:
    print(f'Resultado: {n1/n2}')