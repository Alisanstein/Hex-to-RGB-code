#Converting hex_color_code to RGB code
def hex_string_to_RGB(hex): 
    r = hex[1:3]
    g = hex[3:5]
    b = hex[5:7]
    
    finish = {"r":int(r,16), "g":int(g,16), "b":int(b,16)}

    return finish