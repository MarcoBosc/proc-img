def normalize_RGB():
    while True:
        r = input("Digite um valor para o vermelho.\n")
        g = input("Digite um valor para o verde.\n")
        b = input("Digite um valor para o azul.\n")
        
        red, green, blue = 0, 0, 0

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

    if r != 0:
        red = r / (r + g + b)

    if g != 0:
        green = g / (r + g + b)

    if b != 0:
        blue = b / (r + g + b)

    return red, green, blue, r, g, b

