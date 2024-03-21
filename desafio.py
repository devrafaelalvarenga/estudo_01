#Calculo bonus KPI de 2024

import sys

ano_calculo = 2024
base_calculo_bonus = 1000

#Solicite ao usuario que digite seu nome
try:
    nome_usuario = input('Digite seu nome: ')

    #Verifica se nome contem digitos
    if any(char.isdigit() for char in nome_usuario):
        sys.exit('O nome não deve conter numeros.')
    #Verifica se nome esta vazio    
    elif len(nome_usuario) == 0:
        sys.exit('O nome não pode estar vazio.')
    else:
        print('Nome valido')
except ValueError as e:
    sys.exit(e)                

#Solicite ao usuario que digite o valor do seu salario
try:    
    valor_salario = float(input('Digite o valor do seu salario: '))
    if valor_salario < 0:
        sys.exit('Verifique o valor digitado. Calculo não realizado com valor negativo.')
except ValueError:
    sys.exit('Verifique o valor digitado')

#Solicite ao usuario que digite o valor do bonus recebido (Quantidade salario)
try:    
    valor_bonus = float(input('Digite o valor do bonus recebido: '))
    if valor_bonus < 0:
        sys.exit('Verifique o valor digitado. Calculo não realizado com valor negativo.')
except ValueError:
    sys.exit('Verifique o valor digitado')

#Calcule o valor do bonus final '1000 + salario * bonus'
valor_bonus_final = base_calculo_bonus + (valor_salario * valor_bonus)

#Imprima mensagem personalizada incluindo nome do usuario e valor do bonus
print(f'{nome_usuario.capitalize()} seu bonus em {ano_calculo} é de R${valor_bonus_final:.2f}')
