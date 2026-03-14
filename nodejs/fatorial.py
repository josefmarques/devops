def calcular_fatorial_com_teste_de_mesa(n):
    if n < 0:
        print("Não existe fatorial de número negativo.")
        return None

    # Cabeçalho do Teste de Mesa
    print("\n--- TESTE DE MESA ---")
    print(f"| {'Iteração':<8} | {'Variável (i)':<12} | {'Cálculo Parcial':<15} | {'Resultado Atual':<15} |")
    print("|" + "-"*10 + "|" + "-"*14 + "|" + "-"*17 + "|" + "-"*17 + "|")

    resultado = 1

    # Caso especial para 0 e 1
    if n == 0 or n == 1:
        print(f"| {'1':<8} | {str(n):<12} | {'---':<15} | {'1':<15} |")
    else:
        iteracao = 1
        # range(start, stop, step) -> de n até 1 (o 0 é exclusivo)
        for i in range(n, 0, -1):
            resultado_anterior = resultado
            resultado *= i

            # Exibe a linha da tabela usando f-strings e alinhamento
            # Dentro do loop...
            linha = (
                f"| {str(iteracao):<8} | "
                f"{str(i):<12} | "
                f"{str(resultado_anterior):>7} * {str(i):<5} | "
                f"{str(resultado):<15} |"
            )
            print(linha)
            iteracao += 1

    print("-" * 65 + "\n")
    return resultado


# Interação com o usuário
entrada = input("Digite um número para o Teste de Mesa: ")

if not entrada.isdigit():
    print("Entrada inválida. Por favor, digite um número inteiro.")
else:
    numero = int(entrada)
    final = calcular_fatorial_com_teste_de_mesa(numero)
    if final is not None:
        print(f"=> O fatorial final de {numero} é: {final}")
