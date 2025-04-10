def main():
    """"Recebe um número de testes a serem feitos, por input, e os testes, também por input.
    Calcula quanto tempo irá levar para que a cidade 1 supere, em qtde., a população da cidade 2.
    str (input) -> str (input) -> none."""
    t = int(input())

    # Defesa para valores inválidos de casos:
    if t<1 or t>3000:
        return

    entradas = []
    for i in range(t):
        entrada = input()
        entradas.append(entrada)

    resultados = []
    for i in range(len(entradas)):
        teste = entradas[i].split()
        pop1 = int(teste[0])
        pop2 = int(teste[1])
        taxa1 = float(teste[2])/100
        taxa2 = float(teste[3])/100
        anos = 0
        while pop1<=pop2 and anos <= 100:
            pop1 = int(pop1 + taxa1*pop1)
            pop2 = int(pop2 + taxa2*pop2)
            anos+=1
        resultados.append(anos)

    for resultado in resultados:
        if resultado <= 100:
            print(f"{resultado} anos.")
        else:
            print("Mais de 1 seculo.")

if __name__ == "__main__":
    main()