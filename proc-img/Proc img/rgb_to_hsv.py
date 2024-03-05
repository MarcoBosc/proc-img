def convertion():
    r = input("Digite o valor para o vermelho.\n")
    g = input("Digite o valor para o verde.\n")
    b = input("Digite o valor para o azul.\n")

    h = 0

    try:
        r = int(r)
        g = int(g)
        b = int(b)
    except:
        print("Os valores devem ser números inteiros.")

    def get_max(r, g, b):
        return max(r,g,b)

    def get_min(r, g, b):
        return min(r,g,b)

    if get_max(r, g, b) == r and g >= b:
        h = 60 * ((g-b) / (get_max(r, g, b) - get_min(r, g, b)))

    if get_max(r, g, b) == r and g < b:
        h = (60 * ((g-b) / (get_max(r, g, b) - get_min(r, g, b)))) + 360

    if get_max(r, g, b) == g:
        h = (60 * ((g-b) / (get_max(r, g, b) - get_min(r, g, b)))) + 120
    
    if get_max(r, g, b) == b:
        h = (60 * ((g-b) / (get_max(r, g, b) - get_min(r, g, b)))) + 240

    s = (get_max(r, g, b) - get_min(r, g, b)) / get_max(r, g, b)

    v = get_max(r, g, b)

    print(f"O resultado da conversão do RGB({r, g, b}) para HSV é: HSV({h, s, v})")