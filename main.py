from math import pi, atan

decart_coordinats: list[float] = []


def polar_coords(decart_cordinates: list) -> list:
    '''Преобразует декартовы коодинаты в полярные'''
    polar_coordinates = list()
    x = decart_cordinates[0]
    y = decart_cordinates[1]
    polar_coordinates.append((x**2+y**2)**0.5)
    if x != 0:
        if x < 0:
            if y > 0:
                polar_coordinates.append(pi + atan(y/x))
            else:
                polar_coordinates.append(-pi + atan(y/x))
        else:
            polar_coordinates.append(atan(y/x))
    else:
        if y > 0:
            polar_coordinates.append(pi/2)
        else:
            polar_coordinates.append(-pi/2)
    return polar_coordinates


def transform(input_string: str) -> float:
    '''Преобразует переднное значение в число с плавающей точкой '''
    try:
        out_num = float(input_string)
    except ValueError:
        print('Неверный формат данных. Выполнение программы невозможно')
        exit(1)
    return out_num


def main():
    print('Решение задачи №4  Полярная система координат')
    data = input('Введите декартовы координаты в виде x;y: ')
    if ';' in data:
        data_split = data.split(';')
        decart_coordinats.append(transform(data_split[0]))
        decart_coordinats.append(transform(data_split[1]))
        polar_coordinate = polar_coords(decart_coordinats)
        print(f'Полярный радиус: radius={polar_coordinate[0]:.3f}')
        print(f'Полярный угол: phi={polar_coordinate[1]:.3f}')
    else:
        print('Недостаточно данных. Выполнение программы невозможно')


if __name__ == '__main__':
    main()