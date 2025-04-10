def main():
    """Recebe, por input, uma quantidade de equações e, depois, as equações.
    Por fim, imprime os resultados.
    str(input) -> str(input) -> none"""
    
    n = int(input())
    resultados = []

    for i in range(n):
        entrada = input()
        if entrada == "P=NP": # Pula as entradas deste tipo.
            resultados.append("skipped")
        else:
            numeros = entrada.split("+") # Separa os números das equações de soma pelo sinal.
            resultados.append(int(numeros[0]) + int(numeros[1]))

    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()