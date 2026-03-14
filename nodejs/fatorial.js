const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function calcularFatorialComTesteDeMesa(n) {
  if (n < 0) {
    console.log("Não existe fatorial de número negativo.");
    return;
  }

  // Cabeçalho do Teste de Mesa
  console.log("\n--- TESTE DE MESA ---");
  console.log("| Iteração | Variável (i) | Cálculo Parcial | Resultado Atual |");
  console.log("|----------|--------------|-----------------|-----------------|");

  let resultado = 1;

  // Caso especial para 0 e 1
  if (n === 0 || n === 1) {
    console.log(`|    1     |      ${n}       |      ---        |        1        |`);
  } else {
    let iteracao = 1;
    for (let i = n; i >= 1; i--) {
      const resultadoAnterior = resultado;
      resultado *= i;

      // Exibe a linha da tabela formatada
      console.log(
        `|    ${iteracao.toString().padEnd(5)} |      ${i.toString().padEnd(7)} | ${resultadoAnterior.toString().padStart(7)} * ${i.toString().padEnd(3)} | ${resultado.toString().padEnd(15)} |`
      );
      iteracao++;
    }
  }

  console.log("---------------------\n");
  return resultado;
}

rl.question('Digite um número para o Teste de Mesa: ', (input) => {
  const numero = parseInt(input);

  if (isNaN(numero)) {
    console.log("Entrada inválida.");
  } else {
    const final = calcularFatorialComTesteDeMesa(numero);
    console.log(`=> O fatorial final de ${numero} é: ${final}`);
  }

  rl.close();
});