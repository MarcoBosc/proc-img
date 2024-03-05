def conversion():
    while True:
        try:
            h = float(input("Digite o valor de H (0-360): "))
            s = float(input("Digite o valor de S (0-100): "))
            v = float(input("Digite o valor de V (0-100): "))
            
            if 0 <= h <= 360 and 0 <= s <= 100 and 0 <= v <= 100:
                break
        except:
            print("Os valores de HSV devem ser numéricos.")
    
    R, G, B = 0, 0, 0
    s = s / 100
    v = v / 100

    c = v * s
    
    x = c * (1 - abs((h / 60) % 2 - 1))
    
    m = v - c
    
    if 0 <= h < 60:
        R, G, B = c, x, 0
    
    elif 60 <= h < 120:
        R, G, B = x, c, 0
        
    elif 120 <= h < 180:
        R, G, B = 0, c, x
        
    elif 180 <= h < 240:
        R, G, B = 0, x, c
        
    elif 240 <= h < 300:
        R, G, B = x, 0, c
    
    elif 300 <= h < 360:
        R, G, B = c, 0, x
        
    r, g, b = (R + m) * 255, (G + m) * 255, (B + m) * 255
    
    return round(r), round(g), round(b), int(h) , int(s * 100) , int(v * 100)