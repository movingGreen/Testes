const FATURAMENTO = require('./dados_faturamento.json');

function calcularDadosFaturamento(historico) {
    let media = 0;
    let valores = [];
    let resultado = {
        "Maximo" : 0,
        "Minimo" : 0,
        "DiasAcimaMedia" : 0,
    };

    for (let dadosDia of historico) {
        if (dadosDia.valor == 0) continue;
        
        valores.push(dadosDia.valor);
    }

    valores = valores.sort( function(a, b){return a-b} );
    resultado.Maximo = valores[valores.length - 1];
    resultado.Minimo = valores[0];
    media = valores.reduce( function(total, num){return total += num} ) / valores.length;

    for (let valor of valores) {
        if (valor > media) {
            resultado.DiasAcimaMedia += 1;
        }
    }

    return resultado; 
}

let dadosCalculados = calcularDadosFaturamento(FATURAMENTO);
console.log(dadosCalculados);