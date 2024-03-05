def conversion():
    while True:
        C = input("Digite o valor para o Ciano.\n")
        M = input("Digite o valor para o Magenta.\n")
        Y = input("Digite o valor para o Amarelo.\n")
        K = input("Digite o valor para o Preto.\n")
        try:
            C = int(C)
            M = int(M)
            Y = int(Y)
            K = int(K)
            
            if 0 <= C <= 100 and 0 <= M <= 100 and 0 <= Y <= 100 and 0 <= K <= 100:
                r = round(255 * (1 - C / 100) * (1 - K / 100))
                g = round(255 * (1 - M / 100) * (1 - K / 100))
                b = round(255 * (1 - Y / 100) * (1 - K / 100))
                return r, g, b, C, M, Y, K
            else:
                print("Os valores devem estar entre 0 e 100.")
        except ValueError:
            print("Os valores devem ser números inteiros.")