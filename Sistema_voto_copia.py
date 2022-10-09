governadores = [
    {
        "name": 'Xuxa',
        "number": '10',
        "votes": 0,
    },
    {
        "name": 'Eliana',
        "number": '15',
        "votes": 0,
    },
    {
        "name": 'Angélica',
        "number": '22',
        "votes": 0,
    },
    {
        "name": 'Jaqueline',
        "number": '32',
        "votes": 0,
    }
]

prefeitos = [
    {
        "name": 'Pelé',
        "number": '14',
        "votes": 0,
    },
    {
        "name": 'Maradona',
        "number": '18',
        "votes": 0,
    },
    {
        "name": 'Puskas',
        "number": '26',
        "votes": 0,
    },
    {
        "name": 'Platini',
        "number": '32',
        "votes": 0,
    }
]

def votarPrefeito():
    voto = input('Digite o voto para Prefeito: ')
    candidatoEscolhido = None

    for candidato in prefeitos:
        if(candidato["number"] == voto):
            candidatoEscolhido = candidato
    
    if(candidatoEscolhido is None):
        print('Não encontrado!')
    else:
        if(confirmarVoto(candidatoEscolhido)):
            candidatoEscolhido["votes"] += 1
            print('Voto confirmado!')
        else:
            votarPrefeito()

def votarGovernador():
    voto = input('Digite o voto para Governador: ')
    candidatoEscolhido = None

    for candidato in governadores:
        if(candidato["number"] == voto):
            candidatoEscolhido = candidato
    
    if(candidatoEscolhido is None):
        print('Não encontrado!')

    else:
        if(confirmarVoto(candidatoEscolhido)):
            candidatoEscolhido["votes"] += 1
            print('Voto confirmado!')
        else:
            votarGovernador()
        
def confirmarVoto(candidato):
    confirmar = input(f'Deseja confirmar o seu voto em {candidato["name"]} ? (S ou N):')
    if(confirmar == 'S'):
        return True
    return False

def votar():
    votarGovernador()
    votarPrefeito()

def apuracao():
    print('--------- Governadores ---------')
    for candidato in governadores:
        print('------')
        print(f'Candidato: {candidato["name"]}')
        print(f'Numero: {candidato["number"]}')
        print(f'Votos: {candidato["votes"]}')

    print('--------- Prefeitos ---------')
    for candidato in prefeitos:
        print('------')
        print(f'Candidato: {candidato["name"]}')
        print(f'Numero: {candidato["number"]}')
        print(f'Votos: {candidato["votes"]}')

while True:
    print('1 - VOTAR: \n2 - APURAÇÃO: ')
    opcao = input('ESCOLHA A OPÇÃO: ')
    if opcao == '1':
        votar()
    if opcao == '2':
        apuracao()