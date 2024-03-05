def normalize_RGB():

    r = input("Digite um valor para o vermelho.\n")
    g = input("Digite um valor para o verde.\n")
    b = input("Digite um valor para o azul.\n")
    try:
        r = int(r)
        g = int(g)
        b = int(b)
    except:
        print("Os valores devem ser números inteiros.")

    if r != 0 and g != 0 and b != 0:

        red = r / (r + g + b)

        green = g / (r + g + b)

        blue = b / (r + g + b)
        print(f'O valor do RGB normalizado final é: {red + green + blue}')
    else:
        print(f'O valor do RGB normalizado final é: 0')
