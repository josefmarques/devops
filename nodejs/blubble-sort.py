def bubbleSort_com_teste(arr):
    n = len(arr)
    print(f'\nEstado inicial do array: {arr}')
    print("-" * 60)
    print(f"{'Passo':<8} | {'Par (j, j+1)': <15} | {'Array Atual'}")
    print("-" * 60)

    passo = 1
    # Loop para percorrer o array
    for i in range(n):
        # O último i elementos já estão no lugar, então não precisamos olhar
        for j in range(0, n - i - 1):
            elemento_a = arr[j]
            elemento_b = arr[j + 1]
            par = f"{elemento_a}, {elemento_b}"

            # Comparação: se o da esquerda for maior que o da direita, troca
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                acao = f"Trocou {par}"
            else:
                acao = f"Não trocou {par}"

            # Exibe a linha do teste de mesa
            print(f"{passo:<8} | {par:<15} | {acao:<15} | {arr}")
            passo += 1


# Interação como o usuário
try:
    entrada = input("Digite números separados por espaço (ex: 5 8 9 3): ")
    # Convert a strin de entrada em uma lista de inteiros
    lista = [int(x) for x in entrada.split()]

    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    else:
        resultado = bubbleSort_com_teste(lista)
except ValueError:
    print("Entrada inválida. Digitar números inteiros e separados por espaço.")
