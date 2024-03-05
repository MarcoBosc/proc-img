import norm_rgb, rgb_to_cmyk, rgb_to_hsv, hsv_to_rgb, convert_grey_scale, cmyk_to_rgb

print("Selecione a operação desejada: \n 1 - Normalizar um valor RGB.\n 2 - Converter um valor RGB para HSV.\n 3 - Converter um valor HSV para RGB. \n 4 - Converter um valor RGB para CMYK.\n 5 - Converter CMYK para RGB.\n 6 - Converter um valor RGB para Escala de Cinza.")
option = input("Digite o valor referente a opção escolhida:\n")

match option:
    case "1":
        red, green, blue, r, g, b = norm_rgb.normalize_RGB()
        print(f'O valor do RGB normalizado final é: {red + green + blue}')

    case "2":
        r, g, b, h, s, v = rgb_to_hsv.conversion()
        print(f"O resultado da conversão do RGB{r, g, b} para HSV é: HSV({h}º, {s}%, {v}%)")

    case "3":
        r, g, b, h, s, v = hsv_to_rgb.conversion()
        print(f"O resultado da conversão do HSV({h}º, {s}%, {v}%) para RGB é: RGB{r, g, b}")

    case "4":
        C, M, Y, K, r, g, b = rgb_to_cmyk.conversion()
        print(f"O resultado da conversão do RGB({r, g, b}) para CMYK é: CMYK({C}%, {M}%, {Y}%, {K}%)")


    case "5":
        r, g, b, C, M, Y, K = cmyk_to_rgb.conversion()
        print(f"O resultado da conversão do CMYK({C}%, {M}%, {Y}%, {K}%) para RGB é: RGB({r, g, b})")

    case "6":
        gray_scale, r, g, b = convert_grey_scale.conversion()
        print(f"O pixel RGB{r, g, b} para Grayscale ficaria: {gray_scale}")
    case _:
        print("Opção inválida")