#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa , o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.
# Não foram tratadas condições de digitação do usuário.

# Recebendo os dados do usuário e guarando em variáveis
valorCasa = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = valorCasa / (anos * 12)

# Analisando os dados inseridos para que a condição seja analisada
if prestacao <= salario * (30 / 100):
    print('\33[1;32mA casa que deseja comprar custa R${:.2f} e terá uma parcela de {:.2f} para pagar em {} anos. '
          'EMPRESTIMO APROVADO!\33[m'.format(valorCasa, prestacao, anos))
else:
    print('\33[1;31mSeu empréstimo para comprar uma casa de R${:.2f} foi NEGADO pois a parcela de R${:.2f} ultrapassa '
          ' 30% da sua renda que é de R${:.2f}\33[m'.format(valorCasa, prestacao, salario))