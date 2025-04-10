def main():
    """"Recebe 4 inteiros por input, sendo horas e minutos iniciais e finais, e calcula quanto tempo de intervalo entre esses horários
    str(input), str(input), str(input), str(input) -> none"""
    
    entrada = input().split()
    h_i = int(entrada[0]) # Variável para hora inicial.
    m_i = int(entrada[1]) # Variável para minuto inicial.
    h_f = int(entrada[2]) # Variável para hora final.
    m_f = int(entrada[3]) # Variável para minuto final.

    # Transformo as horas iniciais e finais em minutos, para facilitar a conta.
    inicio = h_i*60 + m_i
    fim = h_f*60 + m_f

    # Se o fim for menor que o início, significa que é uma hora menor do dia seguinte, portanto, somo 24h.
    if fim <= inicio:
        fim += 24*60

    # Cálculo do tempo:
    duracao = fim - inicio
    horas = duracao//60
    minutos = duracao%60

    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

if __name__ == "__main__":
    main()