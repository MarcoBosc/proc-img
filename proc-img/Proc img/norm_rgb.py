def normalize_RGB():

    r = input("Digite um valor para o vermelho.\n")
    g = input("Digite um valor para o verde.\n")
    b = input("Digite um valor para o azul.\n")

    red = 0
    green = 0
    blue = 0
    try:
        r = int(r)
        g = int(g)
        b = int(b)
    except:
        print("Os valores devem ser números inteiros.")

    if r != 0:
        red = r / (r + g + b)

    if g != 0:
        green = g / (r + g + b)

    if b != 0:
        blue = b / (r + g + b)
        
        print(f'O valor do RGB normalizado final é: {red + green + blue}')
    else:
        print(f'O valor do RGB normalizado final é: 0')
