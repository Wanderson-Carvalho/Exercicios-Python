# 64 Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que e a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag.
numero = 1
i = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero != 999:
        i = i + 1
        soma = soma + numero
print('Você digitou {} números e a soma entre eles é {}.'.format(i, soma))