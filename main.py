import math as m

decart_coordinats = ()


def polar_coords(decart_cordinates):
    '''Преобразует декартовы коодинаты в полярные'''
    polar_coordinates = list()
    x = decart_cordinates[0]
    y = decart_cordinates[1]
    polar_coordinates.append((x**2+y**2)**0.5)
    if x != 0:
        if x < 0:
            if y > 0:
                polar_coordinates.append(m.pi + m.atan(y/x))
            else:
                polar_coordinates.append(-m.pi + m.atan(y/x))
        else:
            polar_coordinates.append(m.atan(y/x))
    else:
        if y > 0:
            polar_coordinates.append(m.pi/2)
        else:
            polar_coordinates.append(-m.pi/2)
    return polar_coordinates