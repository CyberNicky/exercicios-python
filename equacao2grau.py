
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


d = b**2 - (4*a*c)

if a == 0 or d < 0: print('equação inválida')

x1 = (-b + (d**(1/2)))/2*a
x2 = (-b - (d**(1/2)))/2*a

print(f'as raizes são {x1} e {x2}')