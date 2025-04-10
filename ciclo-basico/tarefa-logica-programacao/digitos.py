def digitos(n, m):
    """Recebe dois inteiros como entrada e calcula a potência de n^m.
    int, int -> int"""
    
    tam = len(str(n**m)) # Calculo a potência de n^m e transformo o número em string.
    return tam

def main():
    """Recebe um input da quantidade de testes e depois os números para cada teste.
    Por fim, imprime os resultados.
    str(input) -> str(input) -> none"""
    testes = input()
    resultados = []

    for i in range(int(testes)):
        entrada = input()
        numeros = entrada.split()
        n, m = (int(numeros[0]), int(numeros[1]))
        resultados.append(digitos(n,m))

    for i in range(len(resultados)):
        print(resultados[i])

if __name__ == "__main__":
    main()