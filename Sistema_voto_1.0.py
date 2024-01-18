#Cadastro de dados
gov1 = ['Xuxa', '10']
gov2 = ['Eliana', '15']
gov3 = ['Angelica', '22']
gov4 = ['jaqueline', '32']

pre1 = ['Pelé', '14']
pre2 = ['Maradona', '18']
pre3 = ['Puskas', '26']
pre4 = ['Platini', '32']

votosgov1 = 0
votosgov2 = 0
votosgov3 = 0
votosgov4 = 0

votospre1 = 0
votospre2 = 0
votospre3 = 0
votospre4 = 0


#Digitar, ler e verificar a autenticidade dos dados Governador
def governador():
    votoGov = input('Candidato a Governador: ')
    if votoGov == gov1[1]:
        print(gov1[0])
    elif votoGov == gov2[1]:
        print(gov2[0])
    elif votoGov == gov3[1]:
        print(gov3[0])
    elif votoGov == gov4[1]:
        print(gov4[0])
    else:
        print('Digite um número válido')
        governador()

#Confirmar o Voto Governador
def confirmarVotogov():
    confirmaGov = input('Deseja confirmar o voto? ')
    if confirmaGov == ('s'):
        print('Voto confirmado.')
    else:
        governador()
        confirmarVotogov()
        
#Digitar, ler e verificar a autenticidade dos dados Presidente

def presidente():
    votoPre = input('Candidato a Presidente: ')
    if votoPre == pre1[1]:
        print(pre1[0])
    elif votoPre == pre2[1]:
        print(pre2[0])
    elif votoPre == pre3[1]:
        print(pre3[0])
    elif votoPre == pre4[1]:
        print(pre4[0])
    else:
        print('Digite um número válido')
        presidente()

#Confirmar o Voto Presidente
def confirmarVotopre():
    confirmaPre = input('Deseja confirmar o voto? ')
    if confirmaPre == ('s'):
        print('Voto confirmado.')
        print('Fim da votação')
    else:
        presidente()
        confirmarVotopre()

def votar():
    governador()
    confirmarVotogov()
    presidente()
    confirmarVotopre()

def apuracao():
    if governador() == gov1[1]:
        votosgov1 += 1
        print(f'1- {gov1[0]} = {votosgov1}')
    elif governador() == gov2[1]:
        votosgov2 += 1
        print(f'2- {gov1[0]} = {votosgov1}')
    

while True:
    print('1 - VOTAR: \n2 - APURAÇÃO: ')
    opcao = input('ESCOLHA A OPÇÃO: ')
    if opcao == '1':
        votar()
    else:
        apuracao()
    