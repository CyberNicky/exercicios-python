
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite o segundo numero: "))
soma = num1 + num2

print(f'A soma do {num1} + {num2} é: {soma}')



if num1 == num2:
    print('eles são iguais')

elif num1 > num2:
    print(f'{num1} é maior que o {num2}')

else:
    print('eles são diferentes')