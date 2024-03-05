import norm_rgb

def conversion():
    r, g, b, red, green, blue = norm_rgb.normalize_RGB()
    
    h = 0
        
    def get_max(r, g, b):
        return max(r,g,b)

    def get_min(r, g, b):
        return min(r,g,b)

    if get_max(r, g, b) == r and g >= b:
        h = 60 * ((g-b) / (get_max(r, g, b) - get_min(r, g, b)))

    if get_max(r, g, b) == r and g < b:
        h = (60 * ((g-b) / (get_max(r, g, b) - get_min(r, g, b)))) + 360

    if get_max(r, g, b) == g:
        h = (60 * ((b-r) / (get_max(r, g, b) - get_min(r, g, b)))) + 120
    
    if get_max(r, g, b) == b:
        h = (60 * ((r-g) / (get_max(r, g, b) - get_min(r, g, b)))) + 240

    s = (get_max(r, g, b) - get_min(r, g, b)) / get_max(r, g, b)

    v = get_max(red, green, blue) / 255
    print("o max é ", v)
    
    return red, green, blue, int(h + 1), int(s * 100), int(v * 100)
