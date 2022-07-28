let entrada = "testador de string";

function inverterString(string) {
  let stringInvertida = "";

  for (let i = string.length; i > 0; i--) {
    stringInvertida += string[i - 1];
  }

  return stringInvertida;
}

console.log(inverterString(entrada));