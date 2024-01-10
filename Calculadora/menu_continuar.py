

def menu_continuar(funcao):
    while True:
        resposta = input('Deseja continuar: [S/N]: ')[0].upper()
        if resposta in 'nN':
            break
        elif resposta not in 'sSnN':
            print('Opção invalida! Tente novamente.')
            resposta
        else:
            return
        
            
    print('Você saiu. Até logo!')
    



         