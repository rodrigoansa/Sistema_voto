import random
import os

pe = 'Pedra'
pa = 'Papel'
te = 'Tesoura'
bloco = [pe,pa,te]
venceu = 0
empate = 0
perdeu = 0
  
while True:
    print('------------')  
    print('Digite 1 para PEDRA, 2 PAPEL e 3 TESOURA')
    numero = input('ESCOLHA O NÚMERO: ')
    rival = random.choice(bloco)
    if numero == '1':
        os.system("clear")
        print(f'JOGADOR: {pe}')
        print('  X')
        print(f'MAQUINA: {rival}')
        print('------------')  
        if rival == te:
            print('VOCÊ VENCEU!')
            venceu += 1
        if rival == pe:
            print('EMPATOU')
            empate += 1        
        if rival == pa:
            print('VOCÊ PERDEU!')
            perdeu += 1
    if numero == '2':
        os.system("clear")
        print(f'JOGADOR: {pa}')
        print('  X')
        print(f'MAQUINA: {rival}')
        print('------------')      
        if rival == te:
            print('VOCÊ PERDEU!')
            perdeu += 1
        if rival == pe:
            print('VOCÊ VENCEU!')  
            venceu += 1
        if rival == pa:
            print('EMPATOU!')
            empate += 1

    if numero == '3':
        os.system("clear")
        print(f'JOGADOR: {te}')
        print('  X')
        print(f'MAQUINA: {rival}')
        print('------------')    
        if rival == te:
            print('EMPATOU!')
            empate += 1           
        if rival == pe:
            print('VOCÊ PERDEU!')
            perdeu += 1        
        if rival == pa:
            print('VOCÊ VENCEU!')
            venceu += 1 

    print('------------')  
    print(f'VENCEU: {venceu}')
    print(f'EMPATE: {empate}')
    print(f'PERDEU: {perdeu}')    
        