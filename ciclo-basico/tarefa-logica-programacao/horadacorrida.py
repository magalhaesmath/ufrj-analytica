def main():
    """Recebe o número de voltas em um trajeto e o número de placas nele.
    Calcula e imprime o número de placas relativo a cada faixa de conclusão do percurso.
    str (input) -> none"""

    entrada = input()
    numeros = entrada.split()
    v = int(numeros[0])
    n = int(numeros[1])

    # Defesa para valores inválidos:
    if v<1 or n<1:
        return

    total = v*n

    resultados = []
    p = 10
    for i in range(9):
        a = (p*total + 99)//100 # Sempre arredonda para o inteiro imediatamente acima.
        resultados.append(a)
        p+=10

    print(" ".join(map(str, resultados)))


if __name__ == "__main__":
    main()
