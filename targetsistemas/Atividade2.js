let entrada = 144;

function isFibonnaci(numero) {
    let arrayFibonnaci = [0, 1];
    
    if (arrayFibonnaci.includes(numero)) return true;

    for (let i = 2;; i++) {
        arrayFibonnaci[i] = arrayFibonnaci[i - 2] + arrayFibonnaci[i - 1];
        
        if (arrayFibonnaci[i] === numero) return true;
        if (arrayFibonnaci[i] > numero) return false;
    }
}

function mostrarNaTelaSeFibonnaci(numero) {
    if (isFibonnaci(numero)) {
        console.log(`${numero} faz parte da sequência Fibonnaci.`);
        return;
    } 
    console.log(`${numero} não faz parte da sequência Fibonnaci.`);
}

mostrarNaTelaSeFibonnaci(entrada);