import norm_rgb, rgb_to_cmyk, rgb_to_hsv, hsv_to_rgb, convert_grey_scale, cmyk_to_rgb


while True:
    print("Selecione a operação desejada: \n 1 - Normalizar um valor RGB.\n 2 - Converter um valor RGB para HSV.\n 3 - Converter um valor HSV para RGB. \n 4 - Converter um valor RGB para CMYK.\n 5 - Converter CMYK para RGB.\n 6 - Converter um valor RGB para Escala de Cinza.")
    option = input("Digite o valor referente a opção escolhida:\n")

    match option:
        case "1":
            norm_rgb.normalize_RGB()

        case "2":
            rgb_to_hsv.convertion()

        case "3":
            hsv_to_rgb.convertion()

        case "4":
            rgb_to_cmyk.convertion()

        case "5":
            cmyk_to_rgb.convertion()

        case "6":
            convert_grey_scale.convertion()
        case _:
            print("Opção inválida")