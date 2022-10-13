import os

class Politico:
    def _init_(self, name, number):
        self.name = name
        self.number = number
        self.votes = 0
    
    def votar(self):
        self.votes += 1

    def imprimirCandidato(self):
        print('------------')
        print(f'Candidato: {self.name}')
        print(f'Numero: {self.number}')
        print(f'Votos: {self.votes}')


class Votacao:
    def _init_(self, governadores, presidentes):
        self.governadores = governadores
        self.presidentes = presidentes

    def confirmarVoto(self, candidato):
        os.system("clear")
        confirmar = input(f'Deseja confirmar o seu voto em {candidato.name} de número {candidato.number} ? (S ou N):')
        if(confirmar == 'S'):
            return True
        return False
    
    def votarPresidente(self):
        os.system("clear")
        voto = input('Digite o voto para Presidente: ')
        candidatoEscolhido = None

        for candidato in self.presidentes:
            if candidato.number == voto:
                candidatoEscolhido = candidato
        
        if candidatoEscolhido is None:
            print('Não encontrado!')
        else:
            if self.confirmarVoto(candidatoEscolhido):
                candidatoEscolhido.votar()
                print('Voto confirmado!')
            else:
                self.votarPresidente()

    def votarGovernador(self):
        os.system("clear")
        voto = input('Digite o voto para Governador: ')
        candidatoEscolhido = None

        for candidato in self.governadores:
            if candidato.number == voto:
                candidatoEscolhido = candidato
        
        if candidatoEscolhido is None:
            print('Não encontrado!')

        else:
            if self.confirmarVoto(candidatoEscolhido):
                candidatoEscolhido.votar()
                print('Voto confirmado!')
            else:
                self.votarGovernador()

    def votar(self):
        self.votarGovernador()
        self.votarPresidente()

    def apuracao(self):
        os.system("clear")
        print('--------- Governadores ---------')
        for candidato in self.governadores:
            candidato.imprimirCandidato()

        print('--------- Prefeitos ---------')
        for candidato in self.presidentes:
            candidato.imprimirCandidato()

governadores = [
    Politico('Xuxa', '10'),
    Politico('Eliana', '15'),
    Politico('Angelica', '22'),
    Politico('Jaqueline', '32'),
]

presidentes = [
    Politico('Pelé', '14'),
    Politico('Maradona', '18'),
    Politico('Puskas', '26'),
    Politico('Platini', '32'),
]

while True:
    votatao = Votacao(governadores, presidentes)

    print('1 - VOTAR: \n2 - APURAÇÃO: ')
    opcao = input('ESCOLHA A OPÇÃO: ')
    if opcao == '1':
        votatao.votar()
    if opcao == '2':
        votatao.apuracao()