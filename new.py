# pedir o nome e a idade de uma pessoa
# se o nome for Monique e a idade for 18, imprima "Liberada"
# se o nome for Bruno e a idade for 20, imprima "tOPADO"
# se não for nenhum desses dois, imprima "sem permissão"

nome=input('Digite seu nome: ')
idade=input ('Digite sua idade: ')

print(f'{nome} {idade}')


if nome.upper() == "MONIQUE" and idade== "18":
    print("liberada")
elif nome == "bruno" and idade=="20":
    print("topado")

else:
    print("sem permissão")

