const FATURAMENTO = require('./dados_faturamento.json');


function calcularDadosFaturamento(historico) {
    let resultado = {};
    let valores = [];

    for (let dadosDia of historico) {
        if (dadosDia.valor == 0) continue;
        
        valores.push(dadosDia.valor);
        console.log(dadosDia);
    }
    return {
        "minimo" : 0
    };
}

calcularDadosFaturamento(FATURAMENTO);
console.log(FATURAMENTO[0].dia);