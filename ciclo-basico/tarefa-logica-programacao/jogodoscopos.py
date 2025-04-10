def main():
    """"Função que simula um jogo de 3 copos e imprime onde está a moeda.
    Recebe, por input, o número de jogadas, os tipos das jogadas e a posição inicial da moeda.
    Por fim, imprime a posição da moeda ao final das jogadas.
    str (input) -> str (input) -> none"""
    n = int(input())

    # Defesa para valores inválidos de n:
    if n<1 or n>1000:
        return

    inicio = input()

    jogadas = []
    for i in range(n):
        jogadas.append(int(input()))

    # "Switch case" para definir a mesa inicial do jogo, sendo 0 os copos vazios e 1 o copo com a moeda.
    if inicio == "A":
        mesa = [1,0,0]

    if inicio == "B":
        mesa = [0,1,0]

    if inicio == "C":
        mesa = [0,0,1]

    # Vai trocando a posição da moeda de acordo com as jogadas:
    for i in range(len(jogadas)):
        if jogadas[i] == 1:
            a = mesa[1]
            mesa[1] = mesa[0]
            mesa[0] = a

        if jogadas[i] == 2:
            a = mesa[2]
            mesa[2] = mesa[1]
            mesa[1] = a

        if jogadas[i] == 3:
            a = mesa[2]
            mesa[2] = mesa[0]
            mesa[0] = a

    # Descobre a posição da moeda.
    final = mesa.index(1)

    # Imprime a posição final da moeda:
    if final == 0:
        print("A")

    if final == 1:
        print("B")

    if final == 2:
        print("C")

if __name__ == "__main__":
    main()