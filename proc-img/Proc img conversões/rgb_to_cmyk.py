def conversion():
    while True:
        r = input("Digite um valor para vermelho entre 0 e 255: \n")
        g = input("Digite um valor para verde entre 0 e 255: \n")
        b = input("Digite um valor para azul entre 0 e 255: \n")

        try:
            r = int(r)
            g = int(g)
            b = int(b)
            
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                break
            else:
                print("Os valores devem estar entre 0 e 255.")
        except ValueError:
            print("Os valores devem ser números inteiros.")
    if r == 0 and g == 0 and b == 0:
        C, M, Y = 0, 0, 0
        K = 100
        return C, M, Y, K, r, g, b
    R = r / 255
    G =  g / 255
    B = b / 255
    
    K = 1 - max(R, G, B)
    
    C = ((1 - R - K) / (1 - K)) * 100
    
    M = ((1 - G - K) / (1 - K)) * 100
    
    Y = ((1 - B - K) / (1 - K)) * 100
    
    return round(C), round(M), round(Y), round(K * 100), r, g, b