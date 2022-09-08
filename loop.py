# pedir x números e mostrar a soma deles no final

#for i in range(9):

qtd = int(input("Quantos números vc quer somar? "))
soma = 0
for x in range(qtd):
    num = int(input(f"Digite o {x+1}° numero: "))
    soma += num
print(soma)