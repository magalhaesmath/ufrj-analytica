def gerar_fibonacci(limite):
    """"Função que calcula a sequência de Fibonacci até um determinado limite e a retorna através de uma lista.
    int -> list"""
    
    sequencia = [1, 1]
    while sequencia[-1] <= limite:
        sequencia.append(sequencia[-2] + sequencia[-1])
    return sequencia

def main():
    """Recebe um indíce k e retorna o k-ésimo número de Fibonot.
    str(input) -> none"""
    k = int(input())

    # Estimativa para o limite baseado no valor de k
    limite = k * 4
    sequencia_fibonacci = gerar_fibonacci(limite)

    fibonot_atual = 4
    contador = 0

    # Itera até encontrar o k-ésimo número da sequência Fibonot
    while True:
        # Se o número atual não está na sequência Fibonacci, contamos como Fibonot
        if fibonot_atual not in sequencia_fibonacci:
            contador += 1
            if contador == k:
                break
        fibonot_atual += 1  # Incrementa o número atual

    print(fibonot_atual)

if __name__ == "__main__":
    main()