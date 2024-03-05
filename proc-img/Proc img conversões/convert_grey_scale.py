def conversion():
    while True:
        r = input("Digite um valor para o vermelho.\n")
        g = input("Digite um valor para o verde.\n")
        b = input("Digite um valor para o azul.\n")

        try:
            r = int(r)
            g = int(g)
            b = int(b)
            
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                gray_scale = (0.3 * r) + (0.59 * g) + (0.11 * b)
                return gray_scale, r, g, b
            else:
                print("Os valores devem estar entre 0 e 255.")
        except ValueError:
            print("Os valores devem ser números inteiros.")

# referência 3.3 Luminosity Method https://www.baeldung.com/cs/convert-rgb-to-grayscale