def main():
    """Função que recebe a quantidade de dias de vida de uma pessoa e retorna sua idade em anos, meses e dias.
    int -> none"""

    dias = int(input())
    resultados = []
    divisores = [365, 30] # Considerando todos os anos e meses c/ 365 dias e 30 dias, respectivamente.
    resto = dias

    for i in range(3):
        if i < 2: # As duas primeiras divisões serão para encontrar os anos e meses, respectivamente.
            valor = resto // divisores[i]
            resultados.append(valor)
            resto = resto % divisores[i]
        else: # A terceira, e última, operação pega apenas os dias que sobraram.
            resultados.append(resto) 

    print(f"{resultados[0]} ano(s)")
    print(f"{resultados[1]} mes(es)")
    print(f"{resultados[2]} dia(s)")

if __name__ == "__main__":
    main()