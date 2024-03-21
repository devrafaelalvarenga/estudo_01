#Calculo bonus KPI de 2024

ano_calculo = 2024
constante_bonus = 1000

#Solicite ao usuario que digite seu nome
nome_usuario = input('Digite seu nome: ').strip()
if nome_usuario.isdigit():
    print('Verifique o nome digitado')
    exit()
elif len(nome_usuario) == 0:
    print('Verifique o nome digitado')
    exit()   
elif nome_usuario.isspace():
    print('Verifique o nome digitado')
    exit()        

#Solicite ao usuario que digite o valor do seu salario
valor_salario = float(input('Digite o valor do seu salario: '))
if valor_salario < 0:
    print('Verifique o valor digitado')
    exit()

#Solicite ao usuario que digite o valor do bonus recebido (Quantidade salario)
valor_bonus = float(input('Digite o valor do bonus recebido: '))
if valor_bonus < 0:
    print('Verifique o valor digitado')
    exit()

#Calcule o valor do bonus final '1000 + salario * bonus'
valor_bonus_final = constante_bonus + (valor_salario * valor_bonus)

#Imprima mensagem personalizada incluindo nome do usuario e valor do bonus
print(f'{nome_usuario.capitalize()} seu bonus em {ano_calculo} é de R${valor_bonus_final}')
