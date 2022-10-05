#Cadastrar candidato e número
candidato1 = ['Pelé', '10']
candidato2 = ['Maradona', '25']
candidato3 = ['Puskas', '99']
candidato4 = ['Platini', '75']


#Digitar candidato e mostar
def votar():
    Presidente = input('Número: ')
    if Presidente == candidato1[1]:
        print(candidato1[0])
        confirmar = input('Confirmar voto?')
        if confirmar == ('s'):
            print('Voto confirmado.')
        else:
            print(votar())
    elif Presidente == candidato2[1]:
        print(candidato2[0])
        confirmar = input('Confirmar voto?')
        if confirmar == ('s'):
            print('Voto confirmado.')
        else:
            print(votar())
    elif Presidente == candidato3[1]:
        print(candidato3[0])
        confirmar = input('Confirmar voto?')
        if confirmar == ('s'):
            print('Voto confirmado.')
        else:
            print(votar())
    elif Presidente == candidato4[1]:
        print(candidato4[0])
        confirmar = input('Confirmar voto?')
        if confirmar == ('s'):
            print('Voto confirmado.')
        else:
            print(votar())
    else:
        print('Número inválido')
        print(votar())

print(votar())

#Confirmar voto
#Reopetir o processo
#Mostrar resultado