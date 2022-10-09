const mainDiv = document.getElementById('root');

const governadores = [];

const adicionarCandidatos = () => {
    governadores.map(gov => {
        const context = document.createElement('div');
    
        const name = document.createElement('p');
        name.appendChild(document.createTextNode(`Nome: ${gov.name}`))
        
        const number = document.createElement('p');
        number.appendChild(document.createTextNode(`Número: ${gov.number}`))

        context.appendChild(name);
        context.appendChild(number);
        mainDiv.appendChild(context);
    });
}

const renderizarCandidatos = () => {
    fetch('http://localhost:3333/candidatos/governadores')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
      data.governadores.map(governador => governadores.push(governador))
      adicionarCandidatos();
    }).catch(function(err) {
      console.log("ERRO", err);
    });
}

renderizarCandidatos();