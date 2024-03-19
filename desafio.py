#Calculo bonus KPI de 2024

ano_calculo = 2024

#Solicite ao usuario que digite seu nome
nome_usuario = input('Digite seu nome: ')

#Solicite ao usuario que digite o valor do seu salario
valor_salario = float(input('Digite o valor do seu salario: '))

#Solicite ao usuario que digite o valor do bonus recebido (Quantidade salario)
valor_bonus = float(input('Digite o valor do bonus recebido: '))

#Calcule o valor do bonus final '1000 + salario * bonus'
constante_bonus = 1000
valor_bonus_final = constante_bonus + (valor_salario * valor_bonus)

#Imprima o calculo do KPI para o usuario
print(valor_bonus_final)

#Imprima mensagem personalizada incluindo nome do usuario e valor do bonus
print(f'{nome_usuario.capitalize} seu bonus recebido em {ano_calculo} é de R$ {valor_bonus_final}')
