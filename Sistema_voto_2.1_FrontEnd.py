from curses import window
from email.mime import image
from fileinput import filename
import os
from PySimpleGUI import Window, Button, Text, Image, Input

#Fotos
Fxuxa = 'xuxa.png'

#Layout
layout = [
    [Image(filename= Fxuxa)]

]
window = Window(
    'Janela',
    layout=layout
)


gov = ['Xuxa', '11', 'Angelica', '21', 'Sasha', '36']
govVotos = [0,0,0]

pre = ['Pele', '16', 'Maradona', '26', 'Puskas', '42']
preVotos = [0,0,0]

def governador():
    os.system("clear")
    escolha = input('Digite um número para governador: ')


    if escolha == gov[1]:
        print(gov[0])
        govVotos[0] += 1
    elif escolha == gov[3]:
        print(gov[2])
        govVotos[1] += 1
    elif escolha == gov[5]:
        print(gov[4])
        govVotos[2] += 1
    else:
        print('Digite um número válido.')
        governador()
    
    confirma = input('Deseja confirmar o seu voto?:s/n ')
    if confirma == 's':
        presidente()
    else:
        governador()

def presidente():
    os.system("clear")
    escolha = input('Digite um número para presidente: ')


    if escolha == pre[1]:
        print(pre[0])
        preVotos[0] += 1
    elif escolha == pre[3]:
        print(pre[2])
        preVotos[1] += 1
    elif escolha == pre[5]:
        print(pre[4])
        preVotos[2] += 1
    else:
        print('Digite um número válido.')
        presidente()
    
    confirma = input('Deseja confirmar o seu voto?:s/n ')
    if confirma == 's':
        print('FIM.')
    else:
        presidente()
    
def votar():
    governador()
    
def apuracao():
    os.system("clear")
    print('------------------')
    print('  GOVERNADORES')
    print('------------------')
    print(f'Candidado: {gov[0]} Votos: {govVotos[0]}')
    print(f'Candidado: {gov[2]} Votos: {govVotos[1]}')
    print(f'Candidado: {gov[4]} Votos: {govVotos[2]}')

    print('----------------')
    print('  PRESIDENTE')
    print('----------------')
    print(f'Candidado: {pre[0]} Votos: {preVotos[0]}')
    print(f'Candidado: {pre[2]} Votos: {preVotos[1]}')
    print(f'Candidado: {pre[4]} Votos: {preVotos[2]}')
   

while True:
    print('1 - VOTAR: \n2 - APURAÇÃO: ')
    opcao = input('ESCOLHA A OPÇÃO: ')
    if opcao == '1':
        votar()
    if opcao == '2':
        apuracao()