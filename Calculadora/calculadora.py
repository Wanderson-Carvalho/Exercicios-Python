import operacoes as op
from cabecalho_calculadora import cabecalho
from menu_continuar import menu_continuar


def calculadora():
    cabecalho()
    while True:
# Verifica qual operação o usuário deseja e valida se etá entre as operações disponíveis  
        while True:
        
            print(' 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão')
            operacao = int(input('Qual operação você deseja realizar: '))
            if operacao < 1 or operacao > 4:
                print('Opção inválida! tente novamente!')
                print('-' * 50)
                
            else:
                num1 = float(input('Digite o 1º número: '))
                num2 = float(input('Digite o 2º número: '))
                
        # Recebe a operação selecionada pelo usuário e faz a chamada a função da operação
        # que será importada do arquivo operações. A operação irá receber os números digitados
        # pelo usuário para realizar o cálculo correspondente.
                if operacao == 1:
                    operacao = 'Soma'
                    resultado = op.soma(num1, num2)              
                elif operacao == 2:
                    operacao = 'Subtração'
                    resultado = op.subtracao(num1, num2)
                elif operacao == 3:
                    operacao = 'Multiplicação'
                    resultado = op.multiplicao(num1, num2)
                else:
                    operacao = 'Divisão'
                    resultado = op.divisao(num1, num2)
                
                
                print(f'A {operacao} de {num1} e {num2} é = {resultado}')
            
                
            resposta = input('Deseja continuar: [S/N]: ')[0].upper()
            if resposta in 'nN':
                break
                
            elif resposta not in 'sSnN':
                print('Opção invalida! Tente novamente.')
            else:
                print('-' * 50)

        
        return 'Você saiu. Até logo!'
                
                
            
            
            
        
    
      

print(calculadora())