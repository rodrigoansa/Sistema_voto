#Cadastro de dados
gov1 = ['Xuxa', '10']
gov2 = ['Eliana', '15']
gov3 = ['Angelica', '22']
gov4 = ['jaqueline', '32']

pre1 = ['Pelé', '14']
pre2 = ['Maradona', '18']
pre3 = ['Puskas', '26']
pre4 = ['Platini', '32']

#Digitar, ler e verificar a autenticidade dos dados

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

governador()

#Confirmar o Voto
def confirmarVotogov():
    confirmaGov = input('Deseja confirmar o voto? ')
    if confirmaGov == ('s'):
        print('Voto confirmado.')
    else:
        governador()
        confirmarVotogov()
        

confirmarVotogov()

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

presidente()

#Confirmar o Voto
def confirmarVotopre():
    confirmaPre = input('Deseja confirmar o voto? ')
    if confirmaPre == ('s'):
        print('Voto confirmado.')
        print('Fim da votação')
    else:
        presidente()
        confirmarVotopre()

confirmarVotopre()